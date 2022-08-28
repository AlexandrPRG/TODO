from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins, viewsets

from notes.views import Admins
from .models import User
from .serializers import UserModelSerializer


class UserModelViewSet(
        # mixins.ListModelMixin,
    #                mixins.RetrieveModelMixin,
    #                mixins.UpdateModelMixin,
    #                viewsets.GenericViewSet,
        ModelViewSet
    ):
    # renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    # permission_classes = [Admins]
