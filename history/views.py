import requests
import os
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from .models import History, create_histories
from .serializers import HistorySerializer


@api_view(['get', 'post'])
def resolve_histories(request):
    if request.method == 'GET':
        queryset = History.objects.all()
        serializer = HistorySerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HistorySerializer(data=request.data)
        return create_histories(serializer)


@api_view(['patch', 'delete'])
def modify_histories(request, history_id):
    history = History.objects.get(id=history_id)
    if request.method == 'PATCH':
        serializer = HistorySerializer(history, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    else:  # DELETE
        try:
            history.delete()
        except:
            return Response("error occured.", status=status.HTTP_400_BAD_REQUEST)
        return Response("OK", status=status.HTTP_202_ACCEPTED)


@api_view(['get'])
def call_naver_search_api(request):
    """
    naver 지역 검색 API 호출 메서드
    - GET 요청 파라미터 'keyword'(쿼리스트링) 값 필요
    """

    url = "https://openapi.naver.com/v1/search/local.json"
    try:
        params = {'query': request.GET.get('keyword'),
                  'display': 5}
        headers = {"X-Naver-Client-Id": os.environ.get("naver_search_api_clientID"),
                   "X-Naver-Client-Secret": os.environ.get("naver_search_api_clientSecret"),
                   }
        result = requests.get(url, params=params, headers=headers)
    except:
        Response("에러 발생", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(result.json(), status=status.HTTP_200_OK)
