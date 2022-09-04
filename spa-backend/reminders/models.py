from django.db import models


class Reminder(models.Model):

    title = models.CharField(max_length=180)
    note = models.TextField(blank=True)
    done = models.BooleanField()
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
