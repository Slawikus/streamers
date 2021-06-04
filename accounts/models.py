from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from mapbox_location_field.models import LocationField, AddressAutoHiddenField


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("Email"), unique=True)
    paypal_email = models.EmailField(_("PayPal email for payments"), unique=True, blank=True, null=True)
    first_name = models.CharField(_("First name"), max_length=150)
    last_name = models.CharField(_("Last name"), max_length=150)
    location = LocationField(_("Coordinates"), null=True, blank=True)
    address = AddressAutoHiddenField(
        _("Address"), max_length=260, null=True, blank=True
    )
    profile_image = models.ImageField(
        _("Profile image"),
        null=True,
        blank=True,
        upload_to="images/profile_images/",
        height_field=None,
        width_field=None,
        max_length=100,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email

    def get_short_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("account_detail", args=[str(self.id)])
