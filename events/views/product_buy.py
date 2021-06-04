from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse,  reverse_lazy
from django.views.generic import UpdateView

from events.models import Product


class ProductBuyView(UpdateView):
    model = Product
    template_name = "events/event_details/event_detail.html"
    fields = ()
    success_url = reverse_lazy("successful_purchase")

    def post(self, request, *args, **kwargs):
        product = self.get_object()

        return HttpResponseRedirect(reverse("event_detail", args=[product.pk]))
