from django import forms
# from phonenumber_field.modelfields import PhoneNumberField

class ContactForm(forms.Form):
    name = forms.CharField(max_length=64, min_length=1, widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class':'field__input'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder':'Your e-mail', 'class':'field__input'}))
    # phone_number = 
    message = forms.CharField(max_length=2500, widget=forms.Textarea(attrs={'placeholder':'Your message', 'rows': 5, 'class':'text-area field__input'}))