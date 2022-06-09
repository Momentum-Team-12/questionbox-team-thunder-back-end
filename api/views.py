from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import User, Question, Answer
from .serializers import (
    UserSerializer,
    QuestionListSerializer,
    AnswerListSerializer,
    QuestionRetrieveSerializer,
    QuestionDetailSerializer,
    AnswerSerializer,
    AllAnswerSerializer,
    FavoriteQuestionSerializer,
    FavoriteAnswerSerializer,
    )
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from django.db.models.query import QuerySet
from .custom_permissions import (
    ReadOnly,
    )
from rest_framework import generics

from django.db.models import Q
from rest_framework import filters


class UserViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request):
        queryset = User.objects.all().order_by('-id')
        if self.request.user.is_authenticated:
            queryset = queryset.filter(pk=self.request.user.pk)

        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all().order_by('-id')
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
        if self.request.user == serializer.instance.author and serializer.instance.answers.count() == 0:
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

    def perform_create(self, serializer):
        pass

    def perform_update(self, serializer):
        if self.request.user == serializer.instance.author:
            serializer.save()

    def perform_destroy(self, instance):
        if self.request.user == instance.author:
            instance.delete()


class AllQuestionView(viewsets.ViewSet):
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
            search_term = self.request.query_params.get("search")
            if search_term is not None:
                results = Question.objects.filter(
                    Q(title__icontains=search_term) | 
                    Q(description__icontains=search_term))

            else:
                results = self.queryset.all()
            return results.order_by('-id')

    def list(self, request):
        queryset = self.get_queryset()
        serializer = QuestionListSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        question = get_object_or_404(queryset, pk=pk)

        serializer = QuestionRetrieveSerializer(question)
        return Response(serializer.data)


class AllAnswerView(viewsets.ViewSet):
    queryset = Answer.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
            search_term = self.request.query_params.get("search")
            if search_term is not None:
                results = Answer.objects.filter(
                    Q(description__icontains=search_term)
                )

            else:
                results = self.queryset.all()
            return results.order_by('-id')

    def list(self, request):
        queryset = self.get_queryset()
        serializer = AnswerListSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        question = get_object_or_404(queryset, pk=pk)

        serializer = AnswerSerializer(question)
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
        if self.request.user == serializer.instance.author:
            serializer.save()

    def perform_destroy(self, instance):
        if self.request.user == instance.author:
            instance.delete()


# class FavoriteQuestionView(viewsets.ModelViewSet):
#     serializer_class = FavoriteQuestionSerializer
#     permission_classes = (IsAuthenticated,)

#     def get_queryset(self):
#         queryset = self.request.user.favorite_questions.all()
#         serializer = FavoriteQuestionSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def perform_create(self, serializer):
#         question = get_object_or_404(Question, pk=self.kwargs["question_pk"])
#         self.request.user.favorite_questions.add(question)
#         serializer.save()

#     def perform_update(self, serializer):
#         pass

#     def perform_destroy(self, instance):
#         question = get_object_or_404(Question, pk=self.kwargs["question_pk"])
#         self.request.user.favorite_questions.remove()


# class FavoriteAnswerView(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)

#     def list(self, request):
#         queryset = self.request.user.favorite_answers.all()
#         serializer = FavoriteAnswerSerializer(queryset, many=True)

#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = self.request.user.favorite_answers.all()
#         answer = get_object_or_404(queryset, pk=pk)

#         serializer = FavoriteQuestionSerializer(answer)
#         return Response(serializer.data)

class FavoriteQuestionListView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = FavoriteQuestionSerializer

    def get_queryset(self):
        return self.request.user.favorite_questions.all()


class FavoriteAnswerListView(ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = FavoriteAnswerSerializer

    def get_queryset(self):
        return self.request.user.favorite_answers.all()


'''
TO DO:
use retrieveupdateapiview


'''