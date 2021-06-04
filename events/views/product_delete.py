from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from events.models import Product


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = "events/product_delete.html"
    success_url = reverse_lazy("product_list")

    def test_func(self):
        return self.get_object().user == self.request.user
