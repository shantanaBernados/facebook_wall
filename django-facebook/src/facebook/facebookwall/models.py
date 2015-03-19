from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User)
    post = models.TextField()


class Like(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
