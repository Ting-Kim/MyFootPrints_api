from django.urls import path, include
from . import views

app_name = 'history'

urlpatterns = [
    path('', views.resolve_histories, name="user_list"),
]
