from django import forms
from django.core.exceptions import ValidationError


PHONES = ['+375(29)',
          '+375(33)',
          '+375(44)',
          '+375(25)']


def login_validator(value):
    if value and value.isalpha():
        pass
    else:
        raise ValidationError(message='Логин не может содержать числовые значения')


def email_validator(value):
    if not'@' in value:
        raise ValidationError(message='@ - обязательный атрибут')


def phone_validator(value):
    if value[:8] in PHONES and len(value) == 15:
        result = False
    else:
        result = True
    if result:
        raise ValidationError(message='+375(__)_______ ')


class LoginForms(forms.Form):
    username = forms.CharField(label='Username', max_length=15)
    password = forms.CharField(label='Password', max_length=8)


class FormToValidate(forms.Form):
    login = forms.CharField(max_length=15, required=False, validators=[login_validator])
    phone = forms.CharField(max_length=15, required=False, validators=[phone_validator])
    email = forms.CharField(max_length=255, required=False, validators=[email_validator])


