from django.utils import timezone
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class New(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    tags = models.ManyToManyField('Tag', related_name='news')
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    views = models.BigIntegerField(default=0)

    def __str__(self) -> str:
        return self.title