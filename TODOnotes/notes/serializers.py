from rest_framework.serializers import ModelSerializer, StringRelatedField

from notes.models import Project, ToDo
from usersapp.serializers import UserSerializer


class ProjectSerializer(ModelSerializer):
    developers = StringRelatedField(many=True)
    class Meta:
        model = Project
        fields = (
            'name_project',
            'link_project',
            'developers',
            )


class ProjectCustomSerializer(ModelSerializer):
    developers = UserSerializer()
    class Meta:
        model = Project
        exclude = (
            'link_project',
            )


class ToDoModelSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        exclude = ('is_active',)
        # fields = (
        #     'todo_project',
        #     'text_note',
        #     'date_create',
        #     'date_update',
        #     'user_todo',
        #     'is_active',
        # )


class ToDoCustomSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = (
            'text_note',
            'date_create',
            'date_update',
        )
