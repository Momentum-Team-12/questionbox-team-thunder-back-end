from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import User, Question, Answer
from .serializers import (
    UserSerializer,
    QuestionListSerializer,
    QuestionRetrieveSerializer,
    QuestionDetailSerializer,
    AnswerSerializer,
    AllAnswerSerializer,
    )
from rest_framework import viewsets
from django.db.models.query import QuerySet

from .custom_permissions import (
    ReadOnly,
    )


class UserViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request):
        queryset = User.objects.all()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(pk=self.request.user.pk)

        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)

        serializer = UserSerializer(user)
        return Response(serializer.data)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.action in ["list"]:
            return QuestionListSerializer
        if self.action in ["retrieve"]:
            return QuestionRetrieveSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
            if self.request.user.is_authenticated:
                queryset = queryset.filter(author=self.request.user)
        return queryset

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if self.request.user == serializer.instance.author:
            serializer.save()

    def perform_destroy(self, instance):
        if self.request.user == instance.author:
            instance.delete()


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        question = get_object_or_404(Question, pk=self.kwargs["question_pk"])
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
            queryset = queryset.filter(question=question)

        return queryset

    def perform_create(self, serializer):
        question = get_object_or_404(Question, pk=self.kwargs["question_pk"])
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user, question=question)

    def perform_update(self, serializer):
        if self.request.user == serializer.instance.author:
            serializer.save()

    def perform_destroy(self, instance):
        if self.request.user == instance.author:
            instance.delete()


class AnswerListRetrieve(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
            if self.request.user.is_authenticated:
                queryset = queryset.filter(author=self.request.user)
        return queryset

    def perform_update(self, serializer):
        if self.request.user == serializer.instance.author:
            serializer.save()

    def perform_destroy(self, instance):
        if self.request.user == instance.author:
            instance.delete()


class AllQuestionView(viewsets.ViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request):
        queryset = Question.objects.all()
        serializer = QuestionListSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, pk=pk)

        serializer = QuestionRetrieveSerializer(question)
        return Response(serializer.data)


class AllAnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.action in ["list"]:
            return AnswerSerializer
        if self.action in ["retrieve", "update", "partial_update"]:
            return AllAnswerSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        question = get_object_or_404(Question, pk=self.kwargs["question_pk"])
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
            queryset = queryset.filter(question=question)

        return queryset

    def perform_create(self, serializer):
        question = get_object_or_404(Question, pk=self.kwargs["question_pk"])
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user, question=question)

    def perform_update(self, serializer):
        if self.request.user == serializer.instance.question.author:
            serializer.save()

    def perform_destroy(self, instance):
        if self.request.user == instance.author:
            instance.delete()
