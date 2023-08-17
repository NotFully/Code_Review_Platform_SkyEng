from django import forms
from django.contrib.auth.password_validation import validate_password
from django.forms import TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class AdminUserRegistrationForm(UserCreationForm):

    password1 = forms.CharField(validators=[validate_password,],
                                widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    password2 = forms.CharField(validators=[validate_password, ],
                                widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["email"]
        widgets = {}
        for field in fields:
            if field != "password":
                widgets[field] = TextInput(attrs={
                    "placeholder": field.replace("_", " ").title()
                })
        widgets["password"] = PasswordInput(render_value=True,
                                            attrs={'required': False})


class AdminUserUpdateForm(forms.ModelForm):

    password = forms.CharField(label=_("Password"), required=True,
                               validators=[validate_password],
                               widget=PasswordInput(render_value=True))

    class Meta:
        model = User
        fields = ["password"]
        widgets = {}
        for field in fields:
            widgets[field] = TextInput(attrs={"placeholder": field.replace("_", " ").title()})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
