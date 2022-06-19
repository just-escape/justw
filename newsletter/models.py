from django import forms
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Subscriber(models.Model):
    email = models.EmailField(max_length=128, unique=True, null=True)
    subscription_date = models.DateTimeField(auto_now_add=True)
    unsubscription_date = models.DateTimeField(
        null=True, blank=False, default=None)

    def __str__(self):
        return str(self.email)


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'


class MurderSubscription(models.Model):
    submitted = models.DateTimeField(auto_now_add=True)
    contact_name = models.CharField(max_length=256)
    contact_email = models.EmailField(max_length=128)
    contact_number = PhoneNumberField()
    comment = models.TextField(blank=True)


class MurderSubscriptionForm(forms.ModelForm):
    class Meta:
        model = MurderSubscription
        fields = '__all__'
