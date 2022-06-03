from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Question, Answer, Favorite
from .serializers import QuestionSerializer, AnswerSerializer
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet 

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'questions': reverse('api-question-list', request=request, format=format),
        'answers': reverse('api-answer-list', request=request, format=format),
    })

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class  = QuestionSerializer

class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
