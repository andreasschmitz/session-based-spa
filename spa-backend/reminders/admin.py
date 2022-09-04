from django.contrib import admin
from .models import Reminder


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "order", "done")
    list_editable = ("order",)
    ordering = ("order", "-pk")
