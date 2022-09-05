import math

import django.contrib.auth.backends
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase

from mixer.backend.django import mixer
from django.contrib.auth.models import auth
from .views import UserModelViewSet
from notes.views import ProjectModelViewSet, TodoModelViewSet
from .models import User
from notes.models import Project, ToDo


# class TestUserViewSet(TestCase):
#
#     def setUp(self) -> None:
#         self.url = '/api/users/'
#         self.users = {
#             # 'username': 'adm',
#             'first_name': 'fn_test1',
#             'last_name': 'ln_test1',
#             'email': 'emtest@em.com'
#         }
#         self.users_upd = {
#             'first_name':'fn_upd1',
#             'last_name': 'ln_upd1',
#             'email': 'emupd@emupd.com'
#         }
#         self.format = 'json'
#         self.user = User.objects.create(**self.users)
#         self.login = 'admin'
#         self.password = 'password'
#         self.admin = User.objects.create_superuser(self.login, 'adm@mail.ru', self.password)
#
#
#     def test_factory_get_list(self):
#         factory = APIRequestFactory()
#         request = factory.get(self.url)
#         view = UserModelViewSet.as_view({'get':'list'})
#         response = view(request)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_factory_create_guest(self):
#         factory = APIRequestFactory()
#         request = factory.post(
#             self.url,
#             self.users,
#             format=self.format
#         )
#         view = UserModelViewSet.as_view({'post':'update'})
#         response = view(request, pk=2)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_factory_create_admin(self):
#         factory = APIRequestFactory()
#         request = factory.post(
#             self.url,
#             self.users,
#             format=self.format,
#         )
#         force_authenticate(request, self.admin)
#         view = UserModelViewSet.as_view({'post':'update'})
#         response = view(request, pk=1)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_apiclient_detail(self):
#         client = APIClient()
#         response = client.get(f'{self.url}{self.user.id}/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_apiclient_update_guest(self):
#         client = APIClient()
#         response = client.put(f'{self.url}{self.user.id}/', **self.users_upd)
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#
#     def test_apiclient_update_admin(self):
#         client = APIClient()
#         client.force_authenticate(user=self.user)
#         client.login(username=self.login, password=self.password)
#         response = client.put(f'{self.url}{self.user.id}/', self.users_upd, format=self.format)
#         self.assertEqual(self.users['first_name'], self.users_upd['first_name'])
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         client.logout()
#
#     def tearDown(self) -> None:
#         pass
#

# class TestMath(APISimpleTestCase):
#
#     def test_sqrt(self):
#         response = math.sqrt(9)
#         self.assertEqual(response, 3)


class TestProject(APITestCase):
    def setUp(self) -> None:
        self.url = '/api/projects/'
        self.format = 'json'
        self.project_dict = {
            'name_project': 'name2old',
            'link_project': 'http://www.OLDtext-old.git',
        }
        self.project_dict_upd = {
            'name_project': 'name20upd',
            'link_project': 'http://www.NEWtext-new.git',
        }
        self.login = 'admin'
        self.password = 'sdfjlkj12340987'
        self.project = Project.objects.create(**self.project_dict)
        self.admin = User.objects.create_superuser(self.login, self.password)


    def test_apitestcase_list_projects(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_apitestcase_update_admin(self):
        # self.client.login(**{'username': self.login, 'password':self.password})
        self.client.force_login(
            # self,
            self.admin,
            # backend='django.contrib.auth.backends.ModelBackend',
        )
        response = self.client.put(f'{self.url}{self.project.id}/',
                                   self.project_dict_upd)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self) -> None:
        pass


class TestTodoes(APITestCase):
    def setUp(self) -> None:
        self.url = '/api/todoes/'

    def test_apitestcase_list_todoes(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def tearDown(self) -> None:
        pass