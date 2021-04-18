from rest_framework import serializers
from . import models as user_models


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = user_models.User
        fields = ['id', 'username', 'email', 'followers']
