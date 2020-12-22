from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=300)
    date_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=5000)
