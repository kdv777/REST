from rest_framework import viewsets, mixins
from rest_framework.generics import UpdateAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.renderers import JSONRenderer, AdminRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import BasePermission
from django.contrib.auth.hashers import make_password

from todos.models import TODO, Project, User
from todos.serializers import TODOModelSerializer, ProjectModelSerializer, UserModelSerializer, UserSerializer
from users.models import CustomUser
from users.serializers import CustomUserModelSerializer

from todo.filters import ProjectFilter




class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff

class CustomUserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer


class TODOModelViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateAPIView,
                        GenericViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer


class ProjectCustomDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter

# class TodoKwargsFilterView(ListAPIView):
#     serializer_class = TODOModelSerializer
#
#     def get_queryset(self):
#         name = self.kwargs['name']
#         return TODO.objects.filter(name__contains=name)


class ProjectModelViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateAPIView,
                          GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


class UserModelViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateAPIView,
                       GenericViewSet):
    renderer_classes = [AdminRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


class CustomUserModelViewSet(ListModelMixin, RetrieveModelMixin, UpdateAPIView, GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()