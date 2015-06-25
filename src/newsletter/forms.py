__author__ = 'siddiqui'

from django import forms

from .models import SignUp

class ContactForm(forms.Form):
    email = forms.EmailField()
    full_name= forms.CharField()
    message = forms.CharField()


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name