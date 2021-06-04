import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from django.db import models
from django.template.defaultfilters import date, time
from django.urls import reverse
from django.utils.timesince import timesince
from django.utils.translation import ugettext_lazy as _

from . import Event
from .product import Product


class Order(models.Model):
    email = models.EmailField(_("Your email"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='orders')
    order_time = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        created = False if self.pk else True

        super().save(force_insert, force_update, using, update_fields)

        if created:
            data = dict(
                id=self.id,
                ordered_at_date=date(self.order_time),
                ordered_at_time=time(self.order_time),
                ordered_at_timesince=timesince(self.order_time),
                buyer=self.email,
                product=self.product.name,
                product_link=reverse('product_update', args=[self.product.id]),
                amount=str(self.product.price)
            )

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f"updates_stream{self.event.id}", {
                    'type': 'send_notification',
                    'value': json.dumps(data)
                }
            )
