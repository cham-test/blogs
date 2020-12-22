from django.db import models
from django.contrib.auth.models import User

from blog.models import Blog, Post
# Create your models here.


class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subscription_user')
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE, related_name='subscription_blog')


class ReadPost(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='read_post_user')
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='read_post_post')
