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
    author = serializers.SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model = Question
        fields = (
            'id',
            'title',
            'created_at',
            'author',
        )


class QuestionRetrieveSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field="username")

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
    author = serializers.SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model = Question
        fields = (
            'id',
            'title',
            'author',
            'created_at',
            'description',
        )
