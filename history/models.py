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
    location_name = models.CharField(max_length=20)
    score = models.FloatField()
    nutshell = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    road_address = models.CharField(max_length=80)
    visited_date = models.DateField(null=False, default=timezone.now)
    visited_time = models.CharField(
        max_length=15, choices=TIME_CHOICES, default=TIME_DINNER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name="history_user", default=None)

    def update(self, data):
        pass


# def read_histories(request):
    # queryset = History.objects.all()
    # serializer = HistorySerializer(queryset, many=True)
    # return Response(serializer.data)

def create_histories(serializer):
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
