import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User

from users.models import CustomUser
from .views import UserModelViewSet, CustomUserModelViewSet
from .models import User, TODO


class TestAuthorViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {'email': 'ap@mail.ru', 'username': 'Al', 'first_name': 'Александр',
                                                 'last_name': 'Пушкин',  }, format='json')
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/user_set/', {'email': 'ap@mail.ru', 'username': 'Al', 'first_name': 'Александр',
                                                 'last_name': 'Пушкин',  }, format='json')
        admin = CustomUser.objects.create_user('admin', 'admin@admin.com', 'admin123456')
        force_authenticate(request, admin)
        view = CustomUserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        user = CustomUser.objects.create(username='Al', email='ap@mail.ru')
        client = APIClient()
        response = client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    class TestTODOViewSet(APITestCase):
        def test_get_list(self):
            response = self.client.get('/api/TODO/')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
