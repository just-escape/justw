from django.urls import path, re_path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.i18n import i18n_patterns

from pages import views

urlpatterns = i18n_patterns(
    path(r'', views.home, name='home'),
    re_path(r'salles/?$', views.room, name='room'),
    re_path(r'reserver/?$', views.booking, name='booking'),
    re_path(r'carte-cadeau/?$', views.gift_voucher, name='gift-voucher'),
    re_path(r'tarifs/?$', views.pricing, name='pricing'),
    re_path(r'entreprises/?$', views.corporate, name='corporate'),
    re_path(r'faq/?$', views.faq, name='faq'),
    re_path(r'news/?$', views.news, name='news'),
    re_path(r'news1/?$', views.news1, name='news1'),
    re_path(r'404/?$', views.error404, name='404'),
    re_path(r'partenaires/?$', views.partners, name='partners'),
    re_path(r'contact/?$', views.contact, name='contact'),
    re_path(r'desabonnement/?$', views.unsubscribe, name='unsubscribe'),
    re_path(r'acces/?$', views.access, name='access'),
    re_path(r'cgv/?$', views.terms, name='terms'),
    re_path(r'cgu/?$', views.conditions, name='conditions'),

    path('admin/', admin.site.urls),
)

urlpatterns += staticfiles_urlpatterns()
