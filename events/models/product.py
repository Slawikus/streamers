from django.contrib.auth import get_user_model
from django.db import models
from django_resized import ResizedImageField


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="products_user")
    image = ResizedImageField(size=[600, 600], quality=75, upload_to="images/profile_images/")

    def __str__(self):
        return self.name

    def qty_sold(self):
        return self.orders.count()

    def revenue(self):
        return self.qty_sold() * self.price
