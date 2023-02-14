from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from todos.models import TODO, Project, User


class TODOModelSerializer(ModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
