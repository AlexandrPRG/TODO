from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            )


class UserCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'is_superuser',
            'is_staff',
            )