from decimal import Decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.utils import timezone
from django.views.generic import ListView

from events.models import Order
from events.models import Event


class DashboardListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "events/dashboard_list.html"

    def get_context_data(self, *, object_list=None,  **kwargs):
        now = timezone.now()
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.filter(host=self.request.user).filter(event_starts__gt=now).order_by('event_starts')[:5]
        context['orders'] = Order.objects.filter(event__host=self.request.user).order_by('-order_time')[:5]

        context["orders_qty"] = self.get_queryset().count()
        context["total_revenue"] = self.get_queryset().aggregate(
                amount__sum=Coalesce(Sum("product__price"), Decimal("0.00")),
            ).get("amount__sum") if context["orders_qty"] > 0 else 0

        average_revenue_per_order = context["total_revenue"] / context["orders_qty"] if context["orders_qty"] > 0 else 0

        context["average_revenue_per_order"] = str(round(average_revenue_per_order, 2))

        return context
