from django.contrib import admin
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'user', 'created']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'summary', 'genre', 'price', 'amount']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'user', 'post', 'created']


