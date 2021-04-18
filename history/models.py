from django.db import models
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status

TIME_BREAKFAST = 'breakfast'
TIME_LUNCH = 'lunch'
TIME_DINNER = 'dinner'
TIME_CHOICES = (
    (TIME_BREAKFAST, '아침'),
    (TIME_LUNCH, '점심',),
    (TIME_DINNER, '저녁'),
)


class History(models.Model):
    location_name = models.CharField(max_length=20)  # 방문했던 장소 이름
    score = models.FloatField()  # 자신이 생각하는 평점
    nutshell = models.CharField(max_length=50)  # 장소에 대한 한마디
    address = models.CharField(max_length=80)  # 장소 지번 주소
    road_address = models.CharField(max_length=80)  # 장소 도로명 주소
    visited_date = models.DateField(null=False, default=timezone.now)  # 방문 날짜
    visited_time = models.CharField(  # 방문 시각 (아침, 점심, 저녁 중 택1)
        max_length=15, choices=TIME_CHOICES, default=TIME_DINNER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name="history_user", default=None)


def create_histories(serializer):
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
