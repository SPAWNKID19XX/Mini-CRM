from django import forms
from .models import Clients

class NewCustomerForm(forms.Form):
    name = forms.CharField(
        required=True
    )
    email = forms.EmailField()
    phone = forms.CharField()

    def clean(self):
        cleaned_form = super().clean()

        name = cleaned_form.get('name')
        email = cleaned_form.get('email')
        phone = cleaned_form.get('phone')

        if email and Clients.objects.filter(email=email).exists():
            raise forms.ValidationError(f"Email {email} already exists in the database.")  
        return cleaned_form