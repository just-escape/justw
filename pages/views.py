import logging
from datetime import datetime

from django.shortcuts import render
from django.db.utils import IntegrityError
from django.core.mail import send_mail

from justw import settings
from newsletter.forms import EmailForm
from newsletter.models import Subscriber
from salesquote.forms import SalesQuoteForm
from salesquote.models import SalesQuote


def get_lang(request):
    return '' if request.LANGUAGE_CODE == 'fr' else request.LANGUAGE_CODE


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
        for key, value in SalesQuote.PTYPES:
            if key == form.cleaned_data['prestation_type']:
                prestation = value
                break
        alcool = form.cleaned_data['option_cocktail_with_alcool']
        soft = form.cleaned_data['option_cocktail_without_alcool']
        privatisation = form.cleaned_data['option_privatisation']
        date = form.cleaned_data['desired_date']
        comment = form.cleaned_data['comment']

        salesquote = SalesQuote(
            contact_name=name,
            company_name=company,
            contact_email=email,
            contact_number=number,
            prestation_type=form.cleaned_data['prestation_type'],
            option_cocktail_with_alcool=alcool,
            option_cocktail_without_alcool=soft,
            option_privatisation=privatisation,
            desired_date=date,
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
        "Prestation : {}".format(prestation),
        "Cocktail alcoolisé : {}".format("oui" if alcool else "non"),
        "Cocktail non alcoolisé : {}".format("oui" if soft else "non"),
        "Privatisation : {}".format("oui" if privatisation else "non"),
        "Date : {}".format(date if date else 'N/A'),
        "",
        "Commentaire : {}".format(comment if comment else 'N/A'),
    ]
    send_mail(
        'Nouvelle demande de devis de {}'.format(name),
        "\n".join(body_lines),
        'devis@justescape.fr',
        settings.ADMINS,
        fail_silently=True,
    )
    logger.debug('Salesquote recorded')

    return SalesQuoteForm(), False, True


def home(request):
    form, error, success = handle_subscription(request)

    data = {
        'current_page': '',
        'lang': get_lang(request),
        'form': form,
        'unexpected_error': error,
        'subscription_success': success,
    }

    return render(request, 'home.html', data)


def room(request):
    show = request.GET.get('show', None)
    data = {
        'current_page': 'salles',
        'lang': get_lang(request),
        'show': show
    }
    return render(request, 'room.html', data)


def booking(request):
    data = {'current_page': 'reserver', 'lang': get_lang(request)}
    return render(request, 'booking.html', data)


def gift_voucher(request):
    data = {'current_page': 'carte-cadeau', 'lang': get_lang(request)}
    return render(request, 'gift-voucher.html', data)


def pricing(request):
    data = {'current_page': 'tarifs', 'lang': get_lang(request)}
    return render(request, 'pricing.html', data)


def corporate(request):
    form, error, success = handle_salesquote(request)

    data = {
        'current_page': 'entreprises',
        'lang': get_lang(request),
        'form': form,
        'unexpected_error': error,
        'salesquote_success': success,
    }

    return render(request, 'corporate.html', data)


def faq(request):
    data = {'current_page': 'faq', 'lang': get_lang(request)}
    return render(request, 'faq.html', data)


def news(request):
    data = {'current_page': 'news', 'lang': get_lang(request)}
    return render(request, 'news.html', data)


def news1(request):
    data = {'current_page': 'news1', 'lang': get_lang(request)}
    return render(request, 'news1.html', data)


def error404(request):
    data = {'current_page': '404', 'lang': get_lang(request)}
    return render(request, '404.html', data)


def partners(request):
    data = {'current_page': 'partenaires', 'lang': get_lang(request)}
    return render(request, 'partners.html', data)


def contact(request):
    form, error, success = handle_subscription(request)

    data = {
        'current_page': 'contact',
        'lang': get_lang(request),
        'form': form,
        'unexpected_error': error,
        'subscription_success': success,
    }

    return render(request, 'contact.html', data)


def unsubscribe(request):
    form, error, success = handle_unsubscription(request)

    data = {
        'current_page': 'desabonnement',
        'lang': get_lang(request),
        'form': form,
        'unexpected_error': error,
        'subscription_success': success,
    }

    return render(request, 'unsubscribe.html', data)


def access(request):
    data = {'current_page': 'acces', 'lang': get_lang(request)}
    return render(request, 'access.html', data)


def terms(request):
    data = {'current_page': 'cgv', 'lang': get_lang(request)}
    return render(request, 'terms.html', data)


def conditions(request):
    data = {'current_page': 'cgu', 'lang': get_lang(request)}
    return render(request, 'conditions.html', data)
