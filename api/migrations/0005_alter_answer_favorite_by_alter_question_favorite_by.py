# Generated by Django 4.0.5 on 2022-06-09 02:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_user_favorite_answers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='favorite_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='favorite_answers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='favorite_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='favorite_questions', to=settings.AUTH_USER_MODEL),
        ),
    ]
