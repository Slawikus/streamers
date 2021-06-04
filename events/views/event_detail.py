from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView

from events.models import Event


class EventDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Event
    template_name = "events/event_details/event_detail.html"
    context_object_name = "event"

    def test_func(self):
        return self.get_object().host == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = self.get_object().orders.order_by('-order_time').all()

        return context
