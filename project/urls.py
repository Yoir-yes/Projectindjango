from django.urls import path
from .views import post_detail, post_list, add_post
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.post_list.as_view(), name='post_list'),
    path('detail/<int:pk>', post_detail.as_view(), name='detail'),
    path('add_post/',add_post.as_view(), name='add_post'),
]