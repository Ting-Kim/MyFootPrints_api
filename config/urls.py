from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from user import views as user_views
from history import views as history_views


router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('histories/', include('history.urls', namespace='history')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
