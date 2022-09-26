from django_filters import rest_framework as filters
from .models import Project, ToDo

# class ProjectFilter(filters.FilterSet):
#     name = filters.CharFilter(lookup_expr='contains')
#
#     class Meta:
#         model = Project,
#         fields = ['name', 'id']


class TodoFilter(filters.FilterSet):
    # project = filters.UUIDFilter(lookup_expr='exact')
    create = filters.DateFromToRangeFilter()

    class Meta:
        model = ToDo
        fields = ['todo_project', 'text_note', 'date_create']
