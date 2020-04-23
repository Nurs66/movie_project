from django import forms
from .models import Contact
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class ContactForm(forms.ModelForm):
    """From for subscriptions with email"""
    captcha = ReCaptchaField()

    class Meta:
        model = Contact
        fields = ('email', 'captcha')
        widgets = {
            "email": forms.EmailInput(attrs={'class': 'editContent', 'placeholder': 'Your email... '})
         }
        labels = {
            'email': ''
        }
