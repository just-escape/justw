from django.db import models
from django import forms
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class SalesQuote(models.Model):
    submitted = models.DateTimeField(auto_now_add=True)
    contact_name = models.CharField(max_length=128)
    company_name = models.CharField(max_length=128)
    contact_email = models.EmailField(max_length=128)
    contact_number = PhoneNumberField()
    group_size = models.CharField(max_length=128)
    desired_date = models.DateTimeField(null=True, blank=False)
    discount_code = models.CharField(blank=True, null=True, max_length=128)
    comment = models.TextField(blank=True)


class SalesQuoteModelForm(forms.ModelForm):
    class Meta:
        model = SalesQuote
        fields = '__all__'
