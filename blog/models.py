from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')

    class Meta:
        ordering = ['created']



