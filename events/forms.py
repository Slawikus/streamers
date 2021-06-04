from django import forms

from dal import autocomplete
from bootstrap_datepicker_plus import DateTimePickerInput

from .models import Event, Product, Order


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = [
            "host",
            "qr_code",
        ]

        widgets = {
            "event_starts": DateTimePickerInput(),
            "product": autocomplete.ModelSelect2(),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['user']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['email']
