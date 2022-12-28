from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import *


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'content', 'created', 'user', 'comments']


class UserSerializer(serializers.ModelSerializer):
    # posts = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')
    posts = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'posts', 'comments']


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['title', 'author', 'summary', 'genre', 'price', 'amount']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'post', 'created']
