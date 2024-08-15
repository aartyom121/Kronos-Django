from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms
from django.contrib.auth.views import LoginView
from django.forms import TextInput
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", "class": "form-control"}),
    )
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email",)

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
            }),
        }


class CustomLoginView(LoginView):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, "class": "my-input"}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class": "my-input"}),
    )