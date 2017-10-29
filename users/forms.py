from django import forms
from django.contrib.auth import authenticate


class UserLoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        login = cleaned_data['login']
        password = cleaned_data['password']
        user = authenticate(
            username=login,
            password=password
        )
        if user is None:
            raise forms.ValidationError('Invalid credentials')

        self.user = user
        return cleaned_data