from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from events.forms import ProductForm
from events.models import Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    form_class = ProductForm
    model = Product
    template_name = "events/product_create.html"
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs["request"] = self.request
    #     return kwargs
