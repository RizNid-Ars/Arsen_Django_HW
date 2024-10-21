from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title