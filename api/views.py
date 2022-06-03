from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, get_object_or_404
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


class AnswerListCV(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    # def get_queryset(self):
    #     return Answer.objects.filter(answer_id=self.kwargs["answer_pk"])

    # def perform_create(self, serializer, **kwargs):
    #     answer = get_object_or_404(Answer, pk=self.kwargs["answer_pk"])
    #     serializer.save(reviewed_by=self.request.user, answer=answer)
