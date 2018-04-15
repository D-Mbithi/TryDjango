from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    updated = models. DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
