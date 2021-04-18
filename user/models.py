from django.db import models
from django.contrib.auth.models import AbstractUser
from config.settings import AUTH_USER_MODEL


class User(AbstractUser):
    # 유저들끼리의 팔로우 기능
    followers = models.ManyToManyField(
        AUTH_USER_MODEL, related_name="followings", blank=True)
