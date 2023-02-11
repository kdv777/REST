from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet

from .models import TODO, Project, User
from .serializers import TODOModelSerializer, ProjectModelSerializer, UserModelSerializer
from users.models import CustomUser
from users.serializers import CustomUserModelSerializer


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class CustomUserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer
