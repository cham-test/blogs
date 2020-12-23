from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

from .email import Email
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

    def __str__(self):
        return f'{self.blog.user.username}: {self.title}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        email = Email(self)
        if self.pk:
            email.send_update_post_message(self.get_subscribers_email())
        else:
            email.send_new_post_message(self.get_subscribers_email())
        return super().save()

    def get_subscribers_email(self) -> list:
        users = User.objects.filter(subscription_user__blog=self.blog)
        emails = [user.email for user in users]
        return emails

    def delete(self, using=None, keep_parents=False):
        email = Email(self)
        email.send_delete_message(self.get_subscribers_email())
        return super().delete()
