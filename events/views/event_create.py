from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from events.forms import EventForm
from events.models import Event


class EventCreateView(LoginRequiredMixin, CreateView):
    form_class = EventForm
    model = Event
    template_name = "events/event_new.html"
    success_url = reverse_lazy("event_list")

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)
