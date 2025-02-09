from django.urls import path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.i18n import i18n_patterns

from pages import views

urlpatterns = i18n_patterns(
    path('', views.home, name='home'),
    path('salles', views.room, name='room'),
    path('murder-party', views.murder_party, name='murder-party'),
    path('murder-party-redrock-saloon', views.murder_party_redrock_saloon, name='murder-party-redrock-saloon'),
    path('murder-party-le-tournoi-des-sorciers', views.murder_party_le_tournoi_des_sorciers, name='murder-party-le-tournoi-des-sorciers'),
    path('killer-party', views.killer_party, name='killer-party'),
    path('murder-dinner', views.murder_dinner, name='murder-dinner'),
    path('two-rooms', views.two_rooms, name='two-rooms'),
    path('sherlock-vs-moriarty', views.sherlock_vs_moriarty, name='sherlock-vs-moriarty'),
    path('escape-game-evjf', views.escape_game_evjf, name='escape-game-evjf'),
    path('escape-game-evg', views.escape_game_evg, name='escape-game-evg'),
    path('escape-game-anniversaire', views.escape_game_anniversaire, name='escape-game-anniversaire'),
    path('murder-party/qu-est-ce-qu-une-murder-party', views.qu_est_ce_qu_une_murder_party, name='qu-est-ce-qu-une-murder-party'),
    path('reserver', views.booking, name='booking'),
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
    path('blog/salle-reunion-escape-game', views.blog_salle_reunion_escape_game, name='blog-salle-reunion-escape-game'),
    path('blog/seminaire-entreprise-escape-game', views.blog_seminaire_entreprise_escape_game, name='blog-seminaire-entreprise-escape-game'),
    path('blog/seminaire-entreprise-original', views.blog_seminaire_entreprise_original, name='blog-seminaire-entreprise-original'),
    path('blog/salle-seminaire-lille-just-escape', views.blog_salle_seminaire_lille_just_escape, name='blog-salle-seminaire-lille-just-escape'),
    path('blog/jeux-team-building', views.blog_jeux_team_building, name='blog-jeux-team-building'),
    path('blog/animation-murder-party', views.blog_animation_murder_party, name='blog-animation-murder-party'),
    path('blog/animation-entreprise', views.blog_animation_entreprise, name='blog-animation-entreprise'),
    path('blog/idee-animation-seminaire-entreprise', views.blog_idee_animation_seminaire_entreprise, name='blog-idee-animation-seminaire-entreprise'),
    path('blog/idee-animation-soiree-entreprise', views.blog_idee_animation_soiree_entreprise, name='blog-idee-animation-soiree-entreprise'),
    path('blog/location-salle-reunion-lille', views.blog_location_salle_reunion_lille, name='blog-location-salle-reunion-lille'),
    path('blog/escape-game-entreprise', views.blog_escape_game_entreprise, name='blog-escape-game-entreprise'),
    path('blog/guide-indispensable-passionnes-escape-games', views.blog_guide_indispensable_passionnes, name='blog-guide-indispensable-passionnes-escape-games'),
    path('404', views.error404, name='404'),
    path('confirmation', views.confirmation, name='confirmation'),
    path('contact', views.contact, name='contact'),
    path('desabonnement', views.unsubscribe, name='unsubscribe'),
    path('cgv', views.terms, name='terms'),
    path('cgu', views.conditions, name='conditions'),
    path('confirmation-de-commande', views.order_confirmed, name='order_confirmed'),

    prefix_default_language=False,
)

urlpatterns += [path('admin/', admin.site.urls)]

urlpatterns += staticfiles_urlpatterns()
