from pyexpat import model
from rest_framework import serializers
from .models import User, Question, Answer, Favorite

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model: Answer
        fields = (
            'pk',
            'author',
            'description',
            'created_at',
            'question',
            'favorite',
            'accepted',
        )