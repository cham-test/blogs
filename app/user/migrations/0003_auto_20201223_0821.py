# Generated by Django 3.1.4 on 2020-12-23 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201223_0743'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_auto_20201223_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readpost',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='read_post_post', to='blog.post'),
        ),
        migrations.AlterField(
            model_name='readpost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='read_post_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
