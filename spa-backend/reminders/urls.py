from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RemindersViewSet

app_name = "reminders"


router = DefaultRouter()
router.register("reminders", RemindersViewSet, basename="reminders")

urlpatterns = [
    path("", include(router.urls)),
]
