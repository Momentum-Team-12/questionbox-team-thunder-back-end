# Generated by Django 4.0.5 on 2022-06-07 18:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user_favorite_answers_user_favorite_questions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favorite_answers',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favorite_questions',
        ),
        migrations.AddField(
            model_name='answer',
            name='favorite_by',
            field=models.ManyToManyField(related_name='favorite_answers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='favorite_by',
            field=models.ManyToManyField(related_name='favorite_questions', to=settings.AUTH_USER_MODEL),
        ),
    ]
