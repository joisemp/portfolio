from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'required': True}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'required': True}))
    remember_me = forms.BooleanField(required=False)
