from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    images = models.FileField(null=True, blank=True)
    post = models.TextField()
    updated = models. DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail_post", kwargs={'pk': self.pk})
