from django.db import models
# from user.models import User


class History(models.Model):
    location_name = models.CharField(max_length=20)
    score = models.FloatField()
    nutshell = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    road_address = models.CharField(max_length=80)
    visited_at = models.DateTimeField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name="history_user")

# https://velog.io/@brighten_the_way/Django%EC%99%80-Reverse-relations%EA%B3%BC-Relatedname
