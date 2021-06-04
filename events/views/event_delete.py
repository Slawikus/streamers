from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from events.models import Event


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = "events/event_delete.html"
    success_url = reverse_lazy("event_list")

    def test_func(self):
        return self.get_object().is_hosted_by(self.request.user)
