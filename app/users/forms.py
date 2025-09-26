from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UserChangeForm,
)
from django import forms
from django.utils.translation import gettext as _
from phonenumber_field.formfields import PhoneNumberField

from .models import User


class UserCreateForm(UserCreationForm):
    phone = PhoneNumberField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'phone',
            'last_name',
            'first_name',
            'patronymic',
            'password1',
            'password2',
        ]


class UserUpdateForm(UserChangeForm):
    phone = PhoneNumberField()
    password = None

    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label=_('Confirm password'),
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            'email',
            'phone',
            'last_name',
            'first_name',
            'patronymic',
        ]


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
        ]
