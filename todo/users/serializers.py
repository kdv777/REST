from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from todos.models import TODO, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(validated_data['password'])
        )
        user.save()
        return user


class CustomUserModelSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'


class TODOModelSerializer(ModelSerializer):

    class Meta:
        model = TODO
        fields = '__all__'
