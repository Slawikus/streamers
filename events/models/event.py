from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
import qrcode
from django.core.files import File
from io import BytesIO
from PIL import Image, ImageDraw

import uuid

from events.managers import EventManager
from .product import Product
from django.db.models import Count


class Event(models.Model):
    name = models.CharField(_("Stream name"), max_length=40)
    event_starts = models.DateTimeField(_("Stream starts at"))
    description = RichTextField(_("Description"))
    host = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="events",
    )
    shareable_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    qr_code = models.ImageField(upload_to="qr_codes/", blank=True, null=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="events", verbose_name="Product to sell"
    )
    # calling manger into event model
    objects = EventManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("event_detail", args=[str(self.id)])

    def get_absolute_uuid_url(self):

        domain = Site.objects.get_current(self).domain
        path = reverse(
            "public_event_detail_view",
            args=[
                str(self.shareable_id),
            ],
        )
        return f"https://{domain}{path}"

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.get_absolute_uuid_url())
        # making white adjustable square
        canvas = Image.new(
            "RGB", (qrcode_img.pixel_size, qrcode_img.pixel_size), "white"
        )
        draw = ImageDraw.Draw(canvas)
        # putting qr code inside white square
        canvas.paste(qrcode_img)
        file_name = f"qr_code-{self.shareable_id}.png"
        buffer = BytesIO()
        canvas.save(buffer, "PNG")
        self.qr_code.save(file_name, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

    def is_hosted_by(self, user):
        return self.host == user

    class Meta:
        ordering = ["-event_starts"]



