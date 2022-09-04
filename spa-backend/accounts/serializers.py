from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

User = get_user_model()


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Usually, SPA's require some information about the user. Permissions etc.
        fields = ("first_name", "last_name")


class LogInSerializer(serializers.Serializer):

    username = serializers.CharField(write_only=True)
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(self.context["request"], username=username, password=password)

        if user is None:
            raise ValidationError("Unable to log in with provided credentials.")

        attrs["user"] = user
        return attrs
