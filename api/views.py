from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from blog.models import *
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsOwnerOrReadOnly]


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class AuthorDetail(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer


class BooksByAuthor(APIView):
    def get(self, request, id):
        books_by_author = Book.objects.filter(author__id=id)
        serializer = serializers.BookSerializer(books_by_author, many=True)
        return Response(serializer.data)


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]


