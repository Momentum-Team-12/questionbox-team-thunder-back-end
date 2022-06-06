from rest_framework import serializers
from .models import User, Question, Answer


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
            'answers',
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


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field="username")
    question = serializers.SlugRelatedField(read_only=True, slug_field="title")

    class Meta:
        model = Answer
        fields = (
            'pk',
            'author',
            'description',
            'created_at',
            'question',
        )


class AllAnswerSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field="username")
    question = serializers.SlugRelatedField(read_only=True, slug_field="title")

    class Meta:
        model = Answer
        fields = (
            'pk',
            'author',
            'description',
            'created_at',
            'question',
            'accepted',
        )
