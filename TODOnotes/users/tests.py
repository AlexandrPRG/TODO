from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase

from mixer.backend.django import mixer
from django.contrib.auth.models import auth
from .views import UserModelViewSet
from notes.views import ProjectModelViewSet, TodoModelViewSet
from .models import User
from notes.models import Project, ToDo


class TestUserViewSet(TestCase):

    def setUp(self) -> None:
        self.url = 'api/users/'
        self.users = {
            'first_name':'fn_test1',
            'last_name': 'ln_test1',
            'email': 'em1@em.com'
        }
        self.format = 'json'

    def test_factory_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = UserModelViewSet.as_view({'get':'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_factory_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post(
            self.url,
            self.users,
            format=self.format
        )
        view = ProjectModelViewSet.as_view({'post':'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_factory_create_admin(self):
        factory = APIRequestFactory()


    def tearDown(self) -> None:
        pass