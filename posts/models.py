from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=150)
    introduction = models.TextField(max_length=150)
    content = models.TextField(max_length=15000)
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
