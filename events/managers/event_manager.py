from django.db import models

from django.utils import timezone


class EventManager(models.Manager):
    def upcoming_public_events(self):
        now = timezone.now()
        return super().filter(private=False, event_starts__gte=now)

    def upcoming_private_events(self, user):
        now = timezone.now()
        return super().filter(private=True, host=user, event_starts__gte=now)

    def hosted_by(self, user):
        return self.filter(host=user)

    def attended_by(self, user):
        return self.filter(guests__user=user)
