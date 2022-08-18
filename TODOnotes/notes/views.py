from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer

from .models import Project, ToDo
from .serializers import ProjectHyperlinkedModelSerializer, ToDoModelSerializer

class ProjectModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectHyperlinkedModelSerializer


class TodoModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
