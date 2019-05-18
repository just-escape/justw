import phonenumbers
import pytz
from datetime import datetime, timedelta

from django import forms
from justw import settings
from salesquote.models import SalesQuote


def ensure_at_least_tomorrow(value):
    tz = pytz.timezone(settings.TIME_ZONE)
    tomorrow = datetime.now(tz) + timedelta(days=1)
    if tomorrow > value:
        raise forms.ValidationError(
            "Vous ne pouvez pas demander cette prestation avant demain "
            "minimum.")


class BootstrapDateTimePickerInput(forms.DateTimeInput):
    template_name = 'widgets/bootstrap_datetimepicker.html'

    def get_context(self, name, value, attrs):
        datetimepicker_id = 'datetimepicker_{name}'.format(name=name)
        if attrs is None:
            attrs = dict()
        attrs['data-target'] = '#{id}'.format(id=datetimepicker_id)
        attrs['class'] = 'form-control datetimepicker-input'
        context = super().get_context(name, value, attrs)
        context['widget']['datetimepicker_id'] = datetimepicker_id
        return context


class PhoneNumberField(forms.CharField):
    def validate(self, value):
        super().validate(value)
        try:
            p = phonenumbers.parse(value, 'FR')
        except Exception:
            raise forms.ValidationError('Enter a valid phone number.')
        else:
            if not phonenumbers.is_possible_number(p):
                raise forms.ValidationError('Enter a valid phone number.')

            if not phonenumbers.is_valid_number(p):
                raise forms.ValidationError('Enter a valid phone number.')


class SalesQuoteForm(forms.Form):
    contact_name = forms.CharField(
        max_length=128,
        label='Your name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Gérard Manvussa',
                'class': 'form-control',
                'spellcheck': 'false',
            }
        ),
        required=True,
    )
    company_name = forms.CharField(
        max_length=128,
        label='Company name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Just Escape inc.',
                'class': 'form-control',
                'spellcheck': 'false',
            }
        ),
        required=True,
    )
    contact_email = forms.EmailField(
        max_length=128,
        label='Contact email',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'marmitron@justescape.fr',
                'class': 'form-control',
                'spellcheck': 'false',
            }
        ),
        required=True,
    )
    contact_number = PhoneNumberField(
        max_length=16,
        label='Contact number',
        widget=forms.TextInput(
            attrs={
                'placeholder': '06 12 34 56 78',
                'class': 'form-control',
                'spellcheck': 'false',
            }
        ),
        required=True,
    )
    prestation_type = forms.ChoiceField(
        choices=SalesQuote.PTYPES,
        widget=forms.RadioSelect(attrs={'class': 'form-control'}),
        required=True,
    )
    option_cocktail_with_alcool = forms.BooleanField(
        label='Cocktail with alcool',
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-input'}),
        required=False,
    )
    option_cocktail_without_alcool = forms.BooleanField(
        label='Cocktail without alcool',
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-input'}),
        required=False,
    )
    option_privatisation = forms.BooleanField(
        label='Privatisation',
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-input'}),
        required=False,
    )
    desired_date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=BootstrapDateTimePickerInput(
            attrs={'placeholder': 'DD/MM/YYYY hh:mm'}
        ),
        initial=None,
        validators=[ensure_at_least_tomorrow],
        required=False,
    )
    comment = forms.CharField(
        max_length=512,
        label='Comment',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Lorem ipsum',
                'rows': 4,
                'class': 'form-control'
            }
        ),
        required=False,
    )
