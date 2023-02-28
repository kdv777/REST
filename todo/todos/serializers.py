from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from django.contrib.auth.hashers import make_password

from todos.models import TODO, Project, User
from users.models import CustomUser

from rest_framework import serializers


# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
#         write_only_fields = ('password',)
#         read_only_fields = ('id',)
#
#     def create(self, validated_data):
#         user = CustomUser.objects.create(
#             email=validated_data['email'],
#             username=validated_data['username'],
#             password=make_password(validated_data['password'])
#         )
#         user.save()
#         return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ToDoSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = TODO
        fields = '__all__'


class ToDoSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'


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
