from rest_framework import generics
from users.models import User
from .serializers import UserSerializer, UserCustomSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        # self.request.version = self.request.parser_context['kwargs']['version']
        version = self.request.parser_context['request'] #.kwargs.version

        if self.request.version == 'v1':
            return UserCustomSerializer
        return UserSerializer
