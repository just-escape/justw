from django import forms
from django.db import models


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
