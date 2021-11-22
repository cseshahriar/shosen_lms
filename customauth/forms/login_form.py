from django import forms
from django.contrib.auth import (
    get_user_model
)
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
UserModel = get_user_model()


class LMSLoginForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'autofocus': True, 'placeholder': 'Username'}
        )
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password', 'placeholder': 'Password'
            }
        ),

    )
    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }

    def __init__(self, *args, **kwargs):
        super(LMSLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
