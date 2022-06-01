from django.shortcuts import render
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import User, Question, Answer, Favorite
from serializers import AnswerSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('api-user-list', request=request, format=format),
        'questions': reverse('api-question-list', request=request, format=format),
        'records': reverse('api-answer-list', request=request, format=format),
    })

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_destroy(self, instance):
        instance.delete()