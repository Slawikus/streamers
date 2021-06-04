from django.views.generic import CreateView
from django.urls import reverse_lazy

from events.models import Event, Order
from events.forms import OrderForm


class EventPublicDetailView(CreateView):
    form_class = OrderForm
    model = Order
    template_name = "events/event_public_detail.html"
    success_url = reverse_lazy('payment_success')

    def dispatch(self, request, *args, **kwargs):
        self.event = Event.objects.get(shareable_id=self.kwargs.get("shareable_id"))

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = self.event.product
        context['event'] = self.event
        return context

    def form_valid(self, form):
        form.instance.event = self.event
        form.instance.product = self.event.product

        return super().form_valid(form)
