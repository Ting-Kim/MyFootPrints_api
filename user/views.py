from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import serializers
from . import models as user_models


class UserViewSet(ModelViewSet):
    queryset = user_models.User.objects.all()
    serializer_class = serializers.UserSerializer
