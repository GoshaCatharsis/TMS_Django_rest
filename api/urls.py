from django.urls import path
from .views import *


urlpatterns = [
    path('users/', UserList.as_view(), name='api-users'),
    path('users/<int:pk>/', UserDetail.as_view(), name='api-user'),
    path('posts/', PostList.as_view(), name='api-posts'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='api-post')
]