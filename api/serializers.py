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


class QuestionListSerializerForUser(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'title',
            'created_at',
        )


class QuestionDetailSerializerForUser(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'title',
            'created_at',
            'description',
        )


class QuestionListSerializerForAdmin(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'title',
            'created_at',
            'author',
        )


class QuestionDetailSerializerForAdmin(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'title',
            'created_at',
            'author',
            'description',
        )
