from django.urls import path, include
from . import views

app_name = 'user'

urlpatterns = [
    # path('<int:todo_id>/comments/', views.comment_list, name='comment_list'),
    # path('<int:todo_id>/comments/<int:cooment_id>/',
    #  views.comment_detail, name='comment_detail'),
]
