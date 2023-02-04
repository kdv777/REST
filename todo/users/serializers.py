from rest_framework.serializers import ModelSerializer
from .models import CustomUser


class CustomUserModelSerializer(ModelSerializer):


    class Meta:
        model = CustomUser
        fields = ('username', 'firstname', 'lastname', 'email')