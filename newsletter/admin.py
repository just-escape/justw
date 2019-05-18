from django.contrib import admin

from newsletter.models import Subscriber, SubscriberForm


class SubscriberAdmin(admin.ModelAdmin):
    form = SubscriberForm
    list_display = ('email', 'subscription_date', 'unsubscription_date',)
    search_fields = ('email',)

admin.site.register(Subscriber, SubscriberAdmin)
