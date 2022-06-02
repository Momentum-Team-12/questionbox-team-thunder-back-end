from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import User, Question
from .serializers import (
    UserSerializer,
    QuestionListSerializerForUser,
    QuestionDetailSerializerForUser,
    QuestionListSerializerForAdmin,
    QuestionDetailSerializerForAdmin,
    )
from rest_framework import viewsets
from django.db.models.query import QuerySet


@api_view(['GET'])
def api_root(request, format=None):
    if request.user.is_superuser:
        return Response({
            'users': reverse('user-list-api', request=request, format=format),
            'questions': reverse('question-list-api', request=request, format=format),
        })
    else:
        return Response({
            'habits': reverse('habit-list-api', request=request, format=format),
        })


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()

        if not self.request.user.is_superuser:
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
    serializer_class = QuestionListSerializerForUser
    permission_classes = (IsAuthenticated,)

    serializer_action_classes = [
        {
            'list': QuestionListSerializerForUser,
            'create': QuestionListSerializerForUser,
            'retrieve': QuestionDetailSerializerForUser,
            'update': QuestionListSerializerForUser,
            'partial_update': QuestionListSerializerForUser,
            'destroy': QuestionListSerializerForUser
        },
        {
            'list': QuestionListSerializerForAdmin,
            'create': QuestionListSerializerForAdmin,
            'retrieve': QuestionDetailSerializerForAdmin,
            'update': QuestionListSerializerForAdmin,
            'partial_update': QuestionListSerializerForAdmin,
            'destroy': QuestionListSerializerForAdmin
        }
    ]

    def get_serializer_class(self, *args, **kwargs):
        """Instantiate the list of serializers per action from class attribute (must be defined)."""
        kwargs['partial'] = True
        try:
            if self.request.user.is_superuser:
                return self.serializer_action_classes[1][self.action]
            else:
                return self.serializer_action_classes[0][self.action]
        except (KeyError, AttributeError):
            return super(QuestionViewSet, self).get_serializer_class()

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet) and not self.request.user.is_superuser:
            queryset = queryset.filter(author=self.request.user)

        return queryset

    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            serializer.save()

        else:
            serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        user = self.request.user._wrapped if hasattr(self.request.user, '_wrapped') else self.request.user
        if user == instance.author or user.is_superuser:
            instance.delete()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
