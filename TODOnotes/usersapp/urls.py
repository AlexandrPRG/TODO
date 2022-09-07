from django.urls import path
from usersapp.views import UserListAPIView

app_name = 'usersapp'
urlpatterns = [
    path('', UserListAPIView.as_view()),

]
