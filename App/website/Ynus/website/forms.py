from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CompanySignUpForm(UserCreationForm):
    """Form for the new company registration"""
    username = forms.CharField(widget=forms.TextInput(
        attrs=({'placeholder': 'Название компании', 'class': 'input-data-field', 'name': 'company_name'})))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs=({'placeholder': 'Электронная почта', 'class': 'input-data-field', 'name': 'email'})))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs=({'placeholder': 'Пароль', 'class': 'input-data-field', 'name': 'password',
                'minlength': 6, 'maxlength': 15})))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs=({'placeholder': 'Повторите пароль', 'class': 'input-data-field', 'name': 'password',
                'minlength': 6, 'maxlength': 15})))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CompanySignInForm(AuthenticationForm):
    """Form for the company authentification"""
    username = forms.CharField(widget=forms.TextInput(
        attrs=({'placeholder': 'Название компании', 'class': 'input-data-field', 'name': 'company_name'})))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs=({'placeholder': 'Пароль', 'class': 'input-data-field', 'name': 'password',
                'minlength': 6, 'maxlength': 15})))
