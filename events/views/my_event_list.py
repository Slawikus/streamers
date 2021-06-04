from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import ListView

from events.models import Event


class MyEventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "events/my_events.html"
    context_object_name = "events"

    def get_queryset(self):
        now = timezone.now()
        return Event.objects.filter(host=self.request.user).filter(event_starts__lt=now).order_by('-event_starts')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["past"] = True

        return context
