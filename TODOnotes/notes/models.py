from django.db import models
from rest_framework.viewsets import ModelViewSet, ViewSet

from users.models import User


class Project(models.Model):
    name_project = models.CharField(max_length=32, unique=True)
    link_project = models.URLField(verbose_name="GIT link", blank=True)
    developers = models.ManyToManyField(User)

    def __str__(self):
        return self.name_project

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