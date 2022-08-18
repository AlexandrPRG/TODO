from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from notes.models import Project, ToDo


class ProjectHyperlinkedModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = (
            'name_project',
            'link_project',
            'developers',
            )


class ToDoModelSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = (
            'todo_project',
            'text_note',
            'date_create',
            'date_update',
            'user_todo',
            'is_active',
        )
        # exclude = ('is_active')