from rest_framework.viewsets import ModelViewSet

from .models import Reminder
from .serializers import ReminderModelSerializer


# Default permission class requires authenticated users to access this view set
class RemindersViewSet(ModelViewSet):

    serializer_class = ReminderModelSerializer
    queryset = Reminder.objects.all().order_by("order", "-pk")
