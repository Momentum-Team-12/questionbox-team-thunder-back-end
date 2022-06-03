from rest_framework import serializers
from .models import User, Question


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
        )


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'title',
            'created_at',
            'author',
        )


class QuestionRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'title',
            'created_at',
            'author',
            'description',
        )


class QuestionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'title',
            'created_at',
            'description',
        )
