from django.db import models
from django.utils import timezone


class TimestampModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
