from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views as todo_views
from user import views as user_views


router = routers.DefaultRouter()
router.register(r'todos', todo_views.TodoViewSet)
router.register(r'users', user_views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('todos/', include('todo.urls', namespace='todo')),
    # path('users/', include('user.urls', namespace='user')),
    path('histories/', include('history.urls', namespace='history')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
