from django.urls import path
from django.conf import settings


app_name = "accounts"


if settings.CSRF_TOKEN_IN_RESPONSE_BODY is False:
    from .views_wo_csrf_token import LoginAPIView, LogoutAPIView, MeAPIView

    urlpatterns = [
        path("me/", MeAPIView.as_view(), name="me"),
        path("login/", LoginAPIView.as_view(), name="login"),
        path("logout/", LogoutAPIView.as_view(), name="logout"),
    ]
else:
    from .views_with_csrf_token import LoginAPIView, LogoutAPIView, MeAPIView

    urlpatterns = [
        path("me/", MeAPIView.as_view(), name="me"),
        path("login/", LoginAPIView.as_view(), name="login"),
        path("logout/", LogoutAPIView.as_view(), name="logout"),
    ]
