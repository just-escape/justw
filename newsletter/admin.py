from django.contrib import admin

from newsletter.models import Subscriber, SubscriberForm
from newsletter.models import MurderSubscription, MurderSubscriptionForm


class SubscriberAdmin(admin.ModelAdmin):
    form = SubscriberForm
    list_display = ('email', 'subscription_date', 'unsubscription_date',)
    search_fields = ('email',)


class MurderSubscriptionAdmin(admin.ModelAdmin):
    form = MurderSubscriptionForm
    ordering = ('-submitted',)
    list_display = (
        'submitted',
        'contact_name',
        'contact_email',
        'contact_number',
        'comment',
    )
    search_fields = (
        'submitted',
        'contact_name',
        'contact_email',
        'contact_number',
        'comment',
    )

admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(MurderSubscription, MurderSubscriptionAdmin)
