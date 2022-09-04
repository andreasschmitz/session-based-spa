from rest_framework import serializers

from .models import Reminder


class ReminderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ("id", "title", "note", "done", "created_at", "modified_at")
