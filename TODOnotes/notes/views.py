from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, GenericAPIView
from rest_framework.views import View, APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet, ViewSet

from users.models import User
from .models import Project, ToDo
from users.serializers import UserModelSerializer


from .serializers import ProjectHyperlinkedModelSerializer, ToDoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectHyperlinkedModelSerializer


class TodoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer


class ProjectAPIView(ViewSet):

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectHyperlinkedModelSerializer(Project, many=True)
        return Response(serializer.data)


class UserCustomViewSet(ViewSet):
    queryset = ToDo.objects.all()
    serializer_class = UserModelSerializer


class TodoCustomViewSet(ViewSet):

    def destroy(self, request, pk):
        obj = get_object_or_404(ToDo, pk=pk)
        obj.is_active = False
        obj.save()


class ProjectPageNumberPagination(PageNumberPagination):
    page_size  = 10


class ProjectPageNumberPaginationViewSet(PageNumberPagination):
    queryset = Project.objects.all()
    serializer_class = ProjectHyperlinkedModelSerializer
    pagination_class = ProjectPageNumberPagination


class TodoPageNumberPagination(PageNumberPagination):
    page_size  = 20


class TodoPageNumberPaginationViewSet(PageNumberPagination):
    queryset = Project.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = TodoPageNumberPagination
