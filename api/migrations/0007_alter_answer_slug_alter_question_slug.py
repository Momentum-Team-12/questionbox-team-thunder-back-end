# Generated by Django 4.0.5 on 2022-06-02 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_answer_slug_alter_question_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
