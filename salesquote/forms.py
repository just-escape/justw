import phonenumbers
import pytz
from datetime import datetime, timedelta

from django import forms
from django.utils.translation import gettext_lazy as _
from justw import settings
from salesquote.models import SalesQuote


def ensure_at_least_tomorrow(value):
    tz = pytz.timezone(settings.TIME_ZONE)
    tomorrow = datetime.now(tz) + timedelta(days=1)
    if tomorrow > value:
        raise forms.ValidationError(
            _("You can ask for this service tomorrow at least."))


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
            raise forms.ValidationError(_('Enter a valid phone number.'))
        else:
            if not phonenumbers.is_possible_number(p):
                raise forms.ValidationError(_('Enter a valid phone number.'))

            if not phonenumbers.is_valid_number(p):
                raise forms.ValidationError(_('Enter a valid phone number.'))

    def clean(self, value):
        return phonenumbers.format_number(
            phonenumbers.parse(value, 'FR'),
            phonenumbers.PhoneNumberFormat.E164)

class SalesQuoteForm(forms.Form):
    contact_name = forms.CharField(
        max_length=128,
        label=_('Your name'),
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Marmitron'),
                'class': 'form-control',
                'spellcheck': 'false',
            }
        ),
        required=True,
    )
    company_name = forms.CharField(
        max_length=128,
        label=_('Company name'),
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Just Escape'),
                'class': 'form-control',
                'spellcheck': 'false',
            }
        ),
        required=True,
    )
    contact_email = forms.EmailField(
        max_length=128,
        label=_('Contact email'),
        widget=forms.TextInput(
            attrs={
                'placeholder': _('marmitron@justescape.fr'),
                'class': 'form-control',
                'spellcheck': 'false',
            }
        ),
        required=True,
    )
    contact_number = PhoneNumberField(
        max_length=16,
        label=_('Contact number'),
        widget=forms.TextInput(
            attrs={
                'placeholder': _('06 12 34 56 78'),
                'class': 'form-control',
                'spellcheck': 'false',
            }
        ),
        required=True,
    )
    group_size = forms.CharField(
        max_length=128,
        label=_('Group size'),
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Approx. if you don\'t know'),
                'class': 'form-control',
                'spellcheck': 'false',
            }
        ),
        required=True,
    )
    desired_date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        label=_('Desired date'),
        widget=BootstrapDateTimePickerInput(
            attrs={'placeholder': _('DD/MM/YYYY hh:mm')}
        ),
        initial=None,
        validators=[ensure_at_least_tomorrow],
        required=False,
    )
    discount_code = forms.CharField(
        max_length=128,
        label=_('Discount code'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'spellcheck': 'false',
            }
        ),
        required=False,
    )
    comment = forms.CharField(
        max_length=512,
        label=_('Comment'),
        widget=forms.Textarea(
            attrs={
                'placeholder': _(
                    'If you have any request or if there is anything that can '
                    'help us improve your experience'
                ),
                'rows': 4,
                'class': 'form-control'
            }
        ),
        required=False,
    )
