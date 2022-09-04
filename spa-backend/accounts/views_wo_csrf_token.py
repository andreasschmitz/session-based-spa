from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LogInSerializer, UserModelSerializer


class MeAPIView(generics.GenericAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserModelSerializer

    # ensure_csrf_cookie will guarantee that there is a csrftoken cookie in the response
    @method_decorator(ensure_csrf_cookie)
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = self.get_serializer(instance=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)


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

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class LogoutAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response(None, status=status.HTTP_204_NO_CONTENT)
