from django.urls import path, include
from . import views

app_name = 'history'

urlpatterns = [
    path('', views.resolve_histories, name="resolve_histories"),
    path('<int:history_id>/', views.modify_histories, name="modify_histories"),
    path('search/', views.call_naver_search_api, name="naver_search_api"),
]
