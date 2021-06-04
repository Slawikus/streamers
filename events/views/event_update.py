from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView

from events.forms import EventForm
from events.models import Event


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = EventForm
    model = Event
    template_name = "events/event_edit.html"

    def test_func(self):
        return self.get_object().is_hosted_by(self.request.user)
