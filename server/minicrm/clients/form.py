from django import forms
from .models import Clients

class NewCustomerForm(forms.ModelForm):

    class Meta:
        model = Clients
        fields = ['name', 'email', 'phone']

    def clean(self):
        cleaned_form = super().clean()

        email = cleaned_form.get('email')

        if not email:
            return email
        
        cleaned_email = email.strip().lower()

        if cleaned_email[0] == '@' or cleaned_email == '@example.com':
            raise forms.ValidationError("Please insert a valid email address.")

        rec = Clients.objects.filter(email=cleaned_email)

        if self.instance and self.instance.pk:
            rec = rec.exclude(pk=self.instance.pk)

        if rec.exists():
            raise forms.ValidationError(f"Email {email} already exists in the database.")   
         
        return cleaned_form
