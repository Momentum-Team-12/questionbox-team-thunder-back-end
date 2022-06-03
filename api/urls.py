from .views import AnswerDetail, UserList
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'questions/(?P<question_pk>[^/.]+)/answers', AnswerDetail, 'api-answers')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]