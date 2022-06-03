from pyexpat import model
from rest_framework.serializers import ModelSerializer 
from .models import Question, Answer, Favorite

# class UserSerializer(ModelSerializer): 
#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'id',
#         )

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'pk',
            'author',
            'title',
            'description',
            'created_at',
        )        

class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            'pk',
            'author',
            'description',
            'created_at',
            'question',
            # 'favorite',
            # 'accepted',
        )