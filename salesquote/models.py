from django.db import models
from django import forms
from phonenumber_field.modelfields import PhoneNumberField


class SalesQuote(models.Model):
    PTYPES = (
        ('s', 'Escape Game session'),
        ('j', 'Job dating'),
        ('o', 'Other (precise in comments)')
    )

    submitted = models.DateTimeField(auto_now_add=True)
    contact_name = models.CharField(max_length=128)
    company_name = models.CharField(max_length=128)
    contact_email = models.EmailField(max_length=128)
    contact_number = PhoneNumberField()
    prestation_type = models.CharField(
        max_length=1, choices=PTYPES, default=PTYPES[0][0])
    option_cocktail_with_alcool = models.BooleanField(default=False)
    option_cocktail_without_alcool = models.BooleanField(default=False)
    option_privatisation = models.BooleanField(default=False)
    desired_date = models.DateTimeField(null=True, blank=False)
    comment = models.TextField(blank=True)


class SalesQuoteModelForm(forms.ModelForm):
    class Meta:
        model = SalesQuote
        fields = '__all__'
