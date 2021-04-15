from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import History
from .serializers import HistorySerializer


@api_view(['get', 'post'])
def resolve_histories(request):
    if request.method == 'GET':
        queryset = History.objects.all()
        serializer = HistorySerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        pass
