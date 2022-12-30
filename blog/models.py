from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.user.username}: {self.title}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=5000, help_text="Enter a description of the book")
    genre = models.CharField(max_length=100)
    price = models.FloatField()
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True)
    content = models.TextField(blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['created']



