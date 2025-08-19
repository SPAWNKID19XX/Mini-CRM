from django import forms

class NewCustomerForm(forms.Form):
    name = forms.CharField(
        required=True
    )
    email = forms.EmailField()
    phone = forms.CharField()