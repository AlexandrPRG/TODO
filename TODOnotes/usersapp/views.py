from rest_framework import generics
from users.models import User
from .serializers import UserSerializer, UserCustomSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.version == 'v1':
            return UserCustomSerializer
        return UserSerializer