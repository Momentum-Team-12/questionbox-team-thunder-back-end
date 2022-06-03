from .views import UserViewSet, QuestionViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', UserViewSet, 'users')
router.register(r'questions', QuestionViewSet, 'questions')

urlpatterns = [
    path('', include(router.urls)),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
