from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from accounts.models import CustomUser


class Article(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=150)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE,)

    def __str__(self):
        return self.comment


