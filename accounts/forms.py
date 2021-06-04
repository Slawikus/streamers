from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from bootstrap_datepicker_plus import DatePickerInput

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "email",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields["password2"]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "email",
            "paypal_email",
        )
        widgets = {
            "date_of_birth": DatePickerInput(),
        }

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields["password"].widget = forms.HiddenInput()
