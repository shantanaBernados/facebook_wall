from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User)
    post = models.TextField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']


class Like(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'post']
        ordering = ['-date']
