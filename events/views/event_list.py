from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import ListView

from events.models import Event


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "events/all_events_list.html"
    context_object_name = 'events'

    def get_queryset(self):
        now = timezone.now()
        return Event.objects.filter(host=self.request.user).filter(event_starts__gte=now).order_by('event_starts')
