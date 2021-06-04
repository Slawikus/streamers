from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from events.forms import ProductForm
from events.models import Product


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = ProductForm
    model = Product
    template_name = "events/product_edit.html"
    success_url = reverse_lazy("product_list")

    def test_func(self):
        return self.get_object().user == self.request.user

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs["request"] = self.request
    #     return kwargs
