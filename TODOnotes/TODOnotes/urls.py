"""TODOnotes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from rest_framework import permissions
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.authtoken import views

from users.views import UserModelViewSet
from notes.views import ProjectModelViewSet,TodoModelViewSet, UserCustomViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
        openapi.Info(
        title='Notes',
        default_version='v1',
        description='ToDo project',
        contact=openapi.Contact(email='adm@adm.com'),
        license=openapi.License(name='Free MIT LICENSE'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],

)

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todoes', TodoModelViewSet)
router.register('userview', UserCustomViewSet, basename='userview')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    # path('userview/<int:pk>/', UserCustomViewSet.as_view(), name = 'user-view')
    path('api-token-auth/', views.obtain_auth_token),
    # path('', include('usersapp.urls')),
    path('api/users/v1', include('usersapp.urls', namespace='v1')),
    path('api/users/v2', include('usersapp.urls', namespace='v2')),
    path('api/swager<str:format>/', schema_view.without_ui()),
    # path('swager/', schema_view.with_ui('swager')),
    path('redoc/', schema_view.with_ui('redoc')),

    path('graphiql/', GraphQLView.as_view(graphiql=True)),

]
