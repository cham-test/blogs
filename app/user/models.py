from django.db import models
from django.contrib.auth.models import User

from blog.models import Blog, Post
# Create your models here.


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription_user',
                             unique=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='subscription_blog',
                             unique=False)

    def __str__(self):
        return f'{self.user.username}: {self.blog.user.username}'


class ReadPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='read_post_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='read_post_post')
