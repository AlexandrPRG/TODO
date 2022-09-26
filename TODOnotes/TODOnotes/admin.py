from django.contrib import admin

from users.models import User
from notes.models import Project, ToDo


admin.site.register(User)
admin.site.register(Project)
admin.site.register(ToDo)