from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"

    def __str__(self):
        return self.username


class Favorite(models.Model):
    pass


class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('User', on_delete=models.CASCADE, related_name="question_author", max_length=255)
    favorite = models.ForeignKey('Favorite', on_delete=models.CASCADE, related_name="question_favorite", null=True, blank=True)

    def __str__(self):
	    return self.title

class Answer(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE, related_name="users", max_length=255)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name="answers")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
         return(
             f"<Answer pk={self.pk} by author={self.author}>"
         )

    def __str__(self):
	    return self.description