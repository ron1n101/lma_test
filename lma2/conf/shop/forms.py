from django import forms
from phonenumber_field.modelfields import PhoneNumberField

class ContactForm(forms.Form):
    name = forms.CharField(max_length=64, min_lenght=1)
    email = forms.EmailField(required=True, db_index=True)
    phone_number = PhoneNumberField(blank=True, db_index=True)