from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from django.urls import reverse


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Favorite(models.Model):
    pass


class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('User', on_delete=models.CASCADE, related_name="question_author", max_length=255)
    favorite = models.ForeignKey('Favorite', on_delete=models.CASCADE, related_name="question_favorite", max_length=255, null=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)

    def get_absolute_url(self):
        return reverse('questions-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(Question, self).save(*args, **kwargs)


class Answer(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE, related_name="users", max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name="question_question", max_length=255)
    favorite = models.ForeignKey('Favorite', on_delete=models.CASCADE, related_name="answer_favorite", max_length=255, null=True, blank=True)
    accepted = models.BooleanField(default=False)
