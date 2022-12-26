from django.urls import path
from .views import *


urlpatterns = [
    path('users/', UserList.as_view(), name='api-users'),
    path('users/<int:pk>/', UserDetail.as_view(), name='api-user'),
    path('posts/', PostList.as_view(), name='api-posts'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='api-post'),
    path('authors/', AuthorList.as_view(), name='api-authors'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='api-author'),
    path('books/', BookList.as_view(), name='api-books'),
    path('books/<int:pk>/', BookDetail.as_view(), name='api-book'),
]