from rest_framework import serializers
from .models import History


class HistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = History
        fields = [
            'location_name', 'score', 'nutshell', 'address', 'road_address', 'visited_date', 'visited_time', 'created_at', 'updated_at', 'user',
        ]
