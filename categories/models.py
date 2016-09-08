from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
