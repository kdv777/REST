from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserSerializerWithFullName
from django.contrib.auth import get_user_model

User = get_user_model()


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserSerializerWithFullName
        return UserSerializer
