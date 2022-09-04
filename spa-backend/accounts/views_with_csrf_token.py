from django.contrib.auth import login, logout
from django.middleware import csrf
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LogInSerializer, UserModelSerializer


def get_user_csrf_response(request, user):

    user_data = None
    if user is not None and user.is_anonymous is False:
        user_serializer = UserModelSerializer(instance=user)
        user_data = user_serializer.data

    return Response(
        {
            "user": user_data,
            "csrf": csrf.get_token(request),
        },
        status=status.HTTP_200_OK,
    )


class MeAPIView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return get_user_csrf_response(request, self.request.user)


class LoginAPIView(generics.GenericAPIView):

    permission_classes = (AllowAny,)
    serializer_class = LogInSerializer

    # Prevents Login CSRF attacks
    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        # Cleans up previous sessions,rotates CSRF token and persists the user id in the session.
        login(request, user)

        return get_user_csrf_response(request, user)


class LogoutAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        logout(request)
        return get_user_csrf_response(request, None)
