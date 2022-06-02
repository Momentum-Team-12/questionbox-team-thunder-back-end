# Generated by Django 4.0.5 on 2022-06-02 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_favorite_user_created_at_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='favorite',
            field=models.ForeignKey(blank=True, max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer_favorite', to='api.favorite'),
        ),
    ]
