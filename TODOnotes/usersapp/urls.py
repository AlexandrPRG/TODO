from django.urls import path
from usersapp.views import UserListAPIView

app_name = 'usersapp'
urlpatterns = [
    path('api/<str:version>/users/', UserListAPIView.as_view()),

]
