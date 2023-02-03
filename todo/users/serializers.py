from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
