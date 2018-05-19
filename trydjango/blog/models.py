from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone
from markdown_deux import markdown
from django.utils.safestring import mark_safe
from comments.models import Comment


# Create your models here.
class PostManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False).filter(
            published__lte=timezone.now()
        )


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    images = models.FileField(
        upload_to='media/%Y/%m/%d',
        null=True,
        blank=True
        )
    draft = models.BooleanField(default=False)
    published = models.DateTimeField(auto_now=False, auto_now_add=False)
    post = models.TextField()
    updated = models. DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = PostManager()

    class Meta:
        ordering = ['-timestamp', '-updated']

    def __str__(self):
        return self.title

    def get_markdown(self):
        content = self.post
        return mark_safe(markdown(content))

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={'slug': self.slug})

    @property
    def comment(self):
        qs = Comment.objects.filter_by_instance(self)
        return qs

    @property
    def get_content_type(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return content_type


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug)
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance.title, new_slug=new_slug)
    return slug


def pre_save_post_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_reciever, sender=Post)
