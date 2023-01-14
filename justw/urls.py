from django.urls import path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.i18n import i18n_patterns

from pages import views

urlpatterns = i18n_patterns(
    path('', views.home, name='home'),
    path('salles', views.room, name='room'),
    path('murder-party', views.murder_party, name='murder-party'),
    path('murder-party/qu-est-ce-qu-une-murder-party', views.qu_est_ce_qu_une_murder_party, name='qu-est-ce-qu-une-murder-party'),
    path('reserver', views.booking, name='booking'),
    path('reserver-murder-party', views.booking_murder_party, name='booking-murder-party'),
    path('reserver-cyber-party', views.booking_cyber_party, name='booking-cyber-party'),
    path('carte-cadeau', views.gift_voucher, name='gift-voucher'),
    path('tarifs', views.pricing, name='pricing'),
    path('team-building', views.teambuilding, name='teambuilding'),
    path('faq', views.faq, name='faq'),
    path('blog', views.blog, name='blog'),
    path('blog/escape-game-lille-nouvelle-generation', views.blog_escape_game_lille_nouvelle_generation, name='blog-escape-game-lille-nouvelle-generation'),
    path('blog/escape-game-famille-lille', views.blog_escape_game_famille_lille, name='blog-escape-game-famille-lille'),
    path('blog/escape-game-anniversaire-lille', views.blog_escape_game_anniversaire_lille, name='blog-escape-game-anniversaire-lille'),
    path('blog/escape-game-evjf-original', views.blog_escape_game_evjf_original, name='blog-escape-game-evjf-original'),
    path('blog/escape-game-2-joueurs-lille', views.blog_escape_game_2_joueurs_lille, name='blog-escape-game-2-joueurs-lille'),
    path('blog/meilleur-escape-game-lille', views.blog_meilleur_escape_game_lille, name='blog-meilleur-escape-game-lille'),
    path('blog/escape-game-enfant-lille', views.blog_escape_game_enfant_lille, name='blog-escape-game-enfant-lille'),
    path('blog/escape-room-france-guide', views.blog_escape_room_france_guide, name='blog-escape-room-france-guide'),
    path('blog/idees-activites-lille', views.blog_idees_activites_lille, name='blog-idees-activites-lille'),
    path('blog/devis-escape-game', views.blog_devis_escape_game, name='blog-devis-escape-game'),
    path('blog/9-questions-one-brain-escape-game-lille', views.blog_9_questions_one_brain_escape_game_lille, name='blog-9-questions-one-brain-escape-game-lille'),
    path('blog/activite-team-building-escape-game-lille', views.blog_activite_team_building_votre_escape_game_a_lille, name='blog-activite-team-building-escape-game-lille'),
    path('404', views.error404, name='404'),
    path('partenaires', views.partners, name='partners'),
    path('contact', views.contact, name='contact'),
    path('desabonnement', views.unsubscribe, name='unsubscribe'),
    path('cgv', views.terms, name='terms'),
    path('cgu', views.conditions, name='conditions'),
    path('confirmation-de-commande', views.order_confirmed, name='order_confirmed'),

    prefix_default_language=False,
)

urlpatterns += [path('admin/', admin.site.urls)]

urlpatterns += staticfiles_urlpatterns()
