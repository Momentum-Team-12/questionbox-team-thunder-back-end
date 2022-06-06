from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"

    def __str__(self):
        return self.username


class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('User', on_delete=models.CASCADE, related_name="author", max_length=255)

    def __repr__(self):
        return f"<Question title={self.title} pk={self.pk}>"

    def __str__(self):
        return f"{self.title} by {self.author}"


class Answer(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE, related_name="users", max_length=255)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name="answers")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def __repr__(self):
        return(
            f"<Answer pk={self.pk} by author={self.author}>"
        )

    def __str__(self):
        return f"By: {self.author} | {self.description}"
