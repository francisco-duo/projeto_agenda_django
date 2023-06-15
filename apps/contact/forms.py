from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
        )
        widgets = {
            'phone': forms.TextInput(
                attrs={
                    'class': 'classe',
                    'placeholder': 'Celular: (dd) x xxxx - xxxx'
                }
            ),
        }

    def clean_first_name(self, ):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                None,
                ValidationError(
                    'Não digite ABC neste campo.',
                    code='invalid'
                )
            )

        return first_name
