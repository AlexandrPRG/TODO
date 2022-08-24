from django.db import models
from rest_framework.viewsets import ModelViewSet, ViewSet

from users.models import User


class Project(models.Model):
    name_project = models.CharField(blank=True, max_length=64)
    link_project = models.URLField(verbose_name="GIT link")
    developers = models.ManyToManyField(
        User,
        # on_delete = models.CASCADE,

    )


class ToDo(models.Model):
    todo_project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
    )
    text_note = models.TextField(
            blank=True,
    )
    date_create = models.DateField(
        auto_now_add=True,
    )
    date_update = models.DateTimeField(
        auto_now=True,
    )
    user_todo = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    is_active = models.BooleanField(
        default=True,
    )