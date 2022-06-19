import phonenumbers

from django import forms
from newsletter.models import MurderSubscription


class EmailForm(forms.Form):
    email = forms.EmailField(max_length=128, required=True)


class PhoneNumberField(forms.CharField):
    def validate(self, value):
        super().validate(value)
        try:
            p = phonenumbers.parse(value, 'FR')
        except Exception:
            raise forms.ValidationError('Entrez un numéro de téléphone valide.')
        else:
            if not phonenumbers.is_possible_number(p):
                raise forms.ValidationError('Entrez un numéro de téléphone valide.')

            if not phonenumbers.is_valid_number(p):
                raise forms.ValidationError('Entrez un numéro de téléphone valide.')

    def clean(self, value):
        return phonenumbers.format_number(
            phonenumbers.parse(value, 'FR'),
            phonenumbers.PhoneNumberFormat.E164)


class MurderSubscriptionForm(forms.Form):
    contact_name = forms.CharField(
        max_length=128,
        label='Votre nom',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'spellcheck': 'false',
            }
        ),
        required=True,
    )
    contact_email = forms.EmailField(
        max_length=128,
        label='Email de contact',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'contact@justescape.fr',
                'class': 'form-control',
                'spellcheck': 'false',
            }
        ),
        required=True,
    )
    contact_number = PhoneNumberField(
        max_length=16,
        label='Numéro de contact',
        widget=forms.TextInput(
            attrs={
                'placeholder': '06 12 34 56 78',
                'class': 'form-control',
                'spellcheck': 'false',
            }
        ),
        required=True,
    )
    desired_date = forms.CharField(
        max_length=512,
        label='Dates souhaitées',
        widget=forms.Textarea(
            attrs={
                'placeholder': (
                    'Quand voudriez-vous jouer ? Tous les soirs de la semaine ? Seulement le vendredi soir ? Tous les jours sauf le lundi ?'
                ),
                'rows': 4,
                'class': 'form-control'
            }
        ),
        required=False,
    )
    comment = forms.CharField(
        max_length=768,
        label='Commentaire',
        widget=forms.Textarea(
            attrs={
                'placeholder': (
                    'Avez-vous une demande spécifique ? Faites-nous '
                    'part d\'une information particulière pour que '
                    'votre expérience se passe bien.'
                ),
                'rows': 4,
                'class': 'form-control'
            }
        ),
        required=False,
    )
