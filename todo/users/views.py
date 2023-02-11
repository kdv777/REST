from rest_framework.renderers import JSONRenderer, AdminRenderer
from rest_framework.viewsets import ModelViewSet

# from .models import CustomUser
# from .serializers import CustomUserModelSerializer

from todos.models import TODO, Project, User
from todos.serializers import TODOModelSerializer, ProjectModelSerializer, UserModelSerializer
from users.models import CustomUser
from users.serializers import CustomUserModelSerializer

class CustomUserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer

class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class UserModelViewSet(ModelViewSet):
    renderer_classes = [AdminRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class CustomUserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer
