from django.urls import path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.i18n import i18n_patterns

from pages import views

urlpatterns = i18n_patterns(
    path('', views.home, name='home'),
    path('salles', views.room, name='room'),
    path('reserver', views.booking, name='booking'),
    path('reserver-murder-party', views.booking_murder_party, name='booking-murder-party'),
    path('carte-cadeau', views.gift_voucher, name='gift-voucher'),
    path('tarifs', views.pricing, name='pricing'),
    path('team-building', views.teambuilding, name='teambuilding'),
    path('faq', views.faq, name='faq'),
    path('blog', views.news, name='news'),
    path('blog/escape-game-lille-nouvelle-generation', views.news1, name='news1'),
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
