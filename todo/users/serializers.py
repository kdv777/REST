from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import CustomUser
from todos.models import TODO


class CustomUserModelSerializer(ModelSerializer):


    class Meta:
        model = CustomUser
        fields = '__all__'

class TODOModelSerializer(ModelSerializer):

    class Meta:
        model = TODO
        fields = '__all__'

