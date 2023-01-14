import logging
from datetime import datetime

from django.shortcuts import render
from django.db.utils import IntegrityError
from django.core.mail import send_mail

from justw import settings
from newsletter.forms import EmailForm, MurderSubscriptionForm
from newsletter.models import Subscriber, MurderSubscription
from salesquote.forms import SalesQuoteForm
from salesquote.models import SalesQuote


def get_lang(request):
    return '' if request.LANGUAGE_CODE == 'fr' else request.LANGUAGE_CODE + '/'


def handle_subscription(request):
    if request.method != 'POST':
        return EmailForm(), False, False

    logger = logging.getLogger('justw.newsletter')
    logger.debug('Handling a new subscription')

    form = EmailForm(request.POST)
    try:
        logger.debug('Validating subscription form')
        valid = form.is_valid()
    except Exception:
        logger.exception('')
        return form, True, False

    if not valid:
        logger.debug('Subscription form is not valid')
        return form, False, False

    logger.debug('Subscription form is valid')

    try:
        logger.debug('Recording subscription')
        sub = Subscriber(email=form.cleaned_data['email'])
        sub.save()
    except IntegrityError:
        # In case of a duplicated submission we don't show an error
        logger.debug('Email address is already subscribed but whatever')
    except Exception:
        logger.exception('')
        return form, True, False

    logger.debug('Subscription recorded')

    return EmailForm(), False, True


def handle_unsubscription(request):
    if request.method != 'POST':
        return EmailForm(), False, False

    logger = logging.getLogger('justw.newsletter')
    logger.debug('Handling an unsubscription')

    form = EmailForm(request.POST)
    try:
        logger.debug('Validating unsubscription form')
        valid = form.is_valid()
    except Exception:
        logger.exception('')
        return form, True, False

    if not valid:
        logger.debug('Unsubscription form is not valid')
        return form, False, False

    logger.debug('Unsubscription form is valid')

    try:
        logger.debug('Recording unsubscription')
        sub = Subscriber.objects.get(email=form.cleaned_data['email'])
        sub.email = None
        sub.unsubscription_date = datetime.now()
        sub.save()
    except Subscriber.DoesNotExist:
        # Don't show an error
        logger.debug('Email address is not subscribed but whatever')
    except Exception:
        logger.exception('')
        return form, True, False

    logger.debug('Unsubscription recorded')

    return EmailForm(), False, True


def handle_salesquote(request):
    if request.method != 'POST':
        return SalesQuoteForm(), False, False

    logger = logging.getLogger('justw.salesquote')
    logger.debug('Handling a salesquote')

    form = SalesQuoteForm(request.POST)
    try:
        logger.debug('Validating salesquote form')
        valid = form.is_valid()
    except Exception:
        logger.exception('')
        return form, True, False

    if not valid:
        logger.debug('Salesquote form is not valid')
        return form, False, False

    logger.debug('Salesquote form is valid')

    try:
        logger.debug('Recording salesquote')

        name = form.cleaned_data['contact_name']
        company = form.cleaned_data['company_name']
        email = form.cleaned_data['contact_email']
        number = form.cleaned_data['contact_number']
        group_size = form.cleaned_data['group_size']
        service = form.cleaned_data['service']
        date = form.cleaned_data['desired_date']
        budget = form.cleaned_data['budget']
        comment = form.cleaned_data['comment']

        salesquote = SalesQuote(
            contact_name=name,
            company_name=company,
            contact_email=email,
            contact_number=number,
            service=service,
            group_size=group_size,
            desired_date=date,
            budget=budget,
            comment=comment,
        )
        salesquote.save()
    except Exception:
        logger.exception('')
        return form, True, False

    body_lines = [
        "Nom : {}".format(name),
        "Entreprise : {}".format(company),
        "",
        "Email : {}".format(email),
        "Tel : {}".format(number),
        "",
        "Taille du groupe : {}".format(group_size),
        "Prestation : {}".format(service),
        "Date : {}".format(date if date else 'N/A'),
        "Budget : {}".format(budget if budget else 'N/A'),
        "",
        "Commentaire : {}".format(comment if comment else 'N/A'),
    ]
    send_mail(
        "Nouvelle demande de devis de {}".format(name),
        "\n".join(body_lines),
        "devis@justescape.fr",
        settings.ADMINS,
        fail_silently=True,
    )
    logger.debug("Salesquote recorded")

    return SalesQuoteForm(), False, True


def handle_murder_subscription(request):
    if request.method != 'POST':
        return MurderSubscriptionForm(), False, False

    logger = logging.getLogger('justw.murder_subscription')
    logger.debug('Handling a new murder subscription')

    form = MurderSubscriptionForm(request.POST)
    try:
        logger.debug('Validating murder subscription form')
        valid = form.is_valid()
    except Exception:
        logger.exception('')
        return form, True, False

    if not valid:
        logger.debug('Murder subscription form is not valid')
        return form, True, False

    logger.debug('Murder subscription form is valid')

    try:
        logger.debug("Recording murder subscription")

        name = form.cleaned_data['contact_name']
        email = form.cleaned_data['contact_email']
        number = form.cleaned_data['contact_number']
        comment = form.cleaned_data['comment']

        murder_subscription = MurderSubscription(
            contact_name=name,
            contact_email=email,
            contact_number=number,
            comment=comment,
        )
        murder_subscription.save()
    except Exception:
        logger.exception('')
        return form, True, False

    body_lines = [
        "Nom : {}".format(name),
        "Email : {}".format(email),
        "Tel : {}".format(number),
        "Commentaire : {}".format(comment),
    ]
    send_mail(
        "Nouvelle inscription murder party de {}".format(name),
        "\n".join(body_lines),
        "murder-party@justescape.fr",
        settings.ADMINS,
        fail_silently=True,
    )
    logger.debug("Murder subscription recorded")

    return MurderSubscriptionForm(), False, True


def home(request):
    form, error, success = handle_subscription(request)

    data = {
        'current_page': '',
        'lang': get_lang(request),
        'localized': True,
        'form': form,
        'unexpected_error': error,
        'subscription_success': success,
        'cover': True,
    }

    return render(request, 'home.html', data)


def room(request):
    show = request.GET.get('show', None)
    data = {
        'current_page': 'salles',
        'lang': get_lang(request),
        'localized': True,
        'show': show
    }
    return render(request, 'room.html', data)


def murder_party(request):
    form, error, success = handle_murder_subscription(request)

    data = {
        'current_page': 'murder-party',
        'localized': False,
        'form': form,
        'unexpected_error': error,
        'subscription_success': success,
    }
    return render(request, 'murder_party.html', data)


def qu_est_ce_qu_une_murder_party(request):
    data = {
        'current_page': 'qu-est-ce-qu-une-murder-party',
        'lang': get_lang(request),
        'localized': False,
        'cover': True,
        'cover_max_transparency': True,
    }

    r = render(request, 'qu_est_ce_qu_une_murder_party.html', data)
    r['X-Robots-Tag'] = 'noindex'

    return r


def booking(request):
    data = {
        'current_page': 'reserver',
        'lang': get_lang(request),
        'localized': True,
    }

    return render(request, 'booking.html', data)


def booking_murder_party(request):
    data = {
        'current_page': 'reserver-murder-party',
        'lang': get_lang(request),
        'localized': False,
        'noindex': True,
    }

    r = render(request, 'booking_murder_party.html', data)
    r['X-Robots-Tag'] = 'noindex'

    return r


def booking_cyber_party(request):
    data = {
        'current_page': 'reserver-cyber-party',
        'lang': get_lang(request),
        'localized': False,
        'noindex': True,
    }

    r = render(request, 'booking_cyber_party.html', data)
    r['X-Robots-Tag'] = 'noindex'

    return r


def gift_voucher(request):
    data = {'current_page': 'carte-cadeau', 'lang': get_lang(request), 'localized': True}
    return render(request, 'gift-voucher.html', data)


def pricing(request):
    data = {'current_page': 'tarifs', 'lang': get_lang(request), 'localized': True}
    return render(request, 'pricing.html', data)


def teambuilding(request):
    form, error, success = handle_salesquote(request)

    data = {
        'current_page': 'team-building',
        'lang': get_lang(request),
        'localized': False,
        'form': form,
        'unexpected_error': error,
        'salesquote_success': success,
    }

    return render(request, 'teambuilding.html', data)


def faq(request):
    data = {'current_page': 'faq', 'lang': get_lang(request), 'localized': True}
    return render(request, 'faq.html', data)


def blog(request):
    data = {'lang': '', 'localized': False}
    return render(request, 'blog.html', data)


def blog_escape_game_lille_nouvelle_generation(request):
    data = {'lang': '', 'localized': False}
    return render(request, 'blog_escape_game_lille_nouvelle_generation.html', data)


def blog_escape_game_famille_lille(request):
    data = {'lang': '', 'localized': False}
    return render(request, 'blog_escape_game_famille_lille.html', data)


def blog_escape_game_anniversaire_lille(request):
    data = {'lang': '', 'localized': False}
    return render(request, 'blog_escape_game_anniversaire_lille.html', data)


def blog_escape_game_evjf_original(request):
    data = {'lang': '', 'localized': False}
    return render(request, 'blog_escape_game_evjf_original.html', data)


def blog_escape_game_2_joueurs_lille(request):
    data = {'lang': '', 'localized': False}
    return render(request, 'blog_escape_game_2_joueurs_lille.html', data)


def blog_meilleur_escape_game_lille(request):
    data = {'lang': '', 'localized': False}
    return render(request, 'blog_meilleur_escape_game_lille.html', data)


def blog_escape_game_enfant_lille(request):
    data = {'lang': '', 'localized': False}
    return render(request, 'blog_escape_game_enfant_lille.html', data)


def blog_escape_room_france_guide(request):
    data = {'lang': '', 'localized': False}
    return render(request, 'blog_escape_room_france_guide.html', data)


def blog_idees_activites_lille(request):
    data = {'lang': '', 'localized': False}
    return render(request, 'blog_idees_activites_lille.html', data)


def blog_devis_escape_game(request):
    data = {'lang': '', 'localized': False}
    return render(request, 'blog_devis_escape_game.html', data)


def blog_9_questions_one_brain_escape_game_lille(request):
    data = {'lang': '', 'localized': False}
    return render(request, 'blog_9_questions_one_brain_escape_game_lille.html', data)


def blog_activite_team_building_votre_escape_game_a_lille(request):
    data = {'lang': '', 'localized': False}
    return render(request, 'blog_activite_team_building_votre_escape_game_a_lille.html', data)


def error404(request):
    data = {'current_page': '404', 'noindex': True, 'lang': get_lang(request), 'localized': True}
    r = render(request, '404.html', data)
    r['X-Robots-Tag'] = 'noindex'
    return r


def partners(request):
    data = {'current_page': 'partenaires', 'lang': '', 'localized': False}
    return render(request, 'partners.html', data)


def contact(request):
    form, error, success = handle_subscription(request)

    data = {
        'current_page': 'contact',
        'lang': get_lang(request),
        'localized': True,
        'form': form,
        'unexpected_error': error,
        'subscription_success': success,
    }

    return render(request, 'contact.html', data)


def unsubscribe(request):
    form, error, success = handle_unsubscription(request)

    data = {
        'current_page': 'desabonnement',
        'noindex': True,
        'lang': get_lang(request),
        'localized': True,
        'form': form,
        'unexpected_error': error,
        'subscription_success': success,
    }

    r = render(request, 'unsubscribe.html', data)
    r['X-Robots-Tag'] = 'noindex'
    return r


def terms(request):
    data = {'current_page': 'cgv', 'noindex': True, 'lang': get_lang(request), 'localized': True}
    r = render(request, 'terms.html', data)
    r['X-Robots-Tag'] = 'noindex'
    return r


def conditions(request):
    data = {'current_page': 'cgu', 'noindex': True, 'lang': get_lang(request), 'localized': True}
    r = render(request, 'conditions.html', data)
    r['X-Robots-Tag'] = 'noindex'
    return r


def order_confirmed(request):
    data = {'current_page': 'confirmation-de-commande', 'noindex': True, 'lang': get_lang(request), 'localized': True}
    r = render(request, 'order-confirmed.html', data)
    r['X-Robots-Tag'] = 'noindex'
    return r
