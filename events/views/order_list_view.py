from decimal import Decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.views.generic import ListView

from events.models import Order


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "events/order_list.html"
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(event__host=self.request.user).order_by('-order_time')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        context["orders_qty"] = self.get_queryset().count()
        context["total_revenue"] = self.get_queryset().aggregate(
                amount__sum=Coalesce(Sum("product__price"), Decimal("0.00")),
            ).get("amount__sum") if context["orders_qty"] > 0 else 0

        average_revenue_per_order = context["total_revenue"] / context["orders_qty"] if context["orders_qty"] > 0 else 0

        context["average_revenue_per_order"] = str(round(average_revenue_per_order, 2))

        return context


