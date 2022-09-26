from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, GenericAPIView
from rest_framework.views import View, APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework import  permissions
from .serializers import ProjectSerializer, ToDoModelSerializer, ProjectCustomSerializer, \
    ToDoCustomSerializer
from .filters import TodoFilter
from .models import Project, ToDo
from users.serializers import UserModelSerializer
from users.models import User



class Admins(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return True


class Develops(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

class Owners(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated


class ProjectPageNumberPagination(PageNumberPagination):
    page_size  = 10


class TodoPageNumberPagination(PageNumberPagination):
    page_size  = 20


class TodoPageNumberPaginationViewSet(PageNumberPagination):
    queryset = Project.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = TodoPageNumberPagination


class ProjectModelViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    pagination_class = ProjectPageNumberPagination
    permission_classes = [Admins, Owners]

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return ProjectCustomViewSet

    # def get_queryset(self):
    #     query_set = Project.objects.all()
    #     name = self.request.query_params("name_project", None)
    #     if name:
    #         query_set = query_set.filter(name_project__contains=name)
    #     return query_set

class TodoModelViewSet(ModelViewSet):
    serializer_class = ToDoModelSerializer
    queryset = ToDo.objects.all()
    pagination_class = TodoPageNumberPaginationViewSet
    filterset_class = TodoFilter
    permission_classes = [Admins, Develops, Owners]

    def destroy(self, request, *args, **kwargs):
        try:
            instanse = self.get_object()
            instanse.is_active = False
            instanse.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectAPIView(ViewSet):

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(Project, many=True)
        return Response(serializer.data)


class UserCustomViewSet(ViewSet):
    queryset = ToDo.objects.all()
    serializer_class = UserModelSerializer

class ProjectCustomViewSet(ViewSet):
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return ProjectCustomSerializer
        return ProjectSerializer


class TodoCustomViewSet(ViewSet):

    def destroy(self, request, pk):
        obj = get_object_or_404(ToDo, pk=pk)
        obj.is_active = False
        obj.save()

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return ToDoCustomSerializer
        return ToDoModelSerializer


class ProjectPageNumberPaginationViewSet(PageNumberPagination):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectPageNumberPagination
