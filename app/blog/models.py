from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
# Create your models here.


class Blog(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.id])


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=300)
    date_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=5000)

    class Meta:
        ordering = ('-date_time',)
