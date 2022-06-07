"""questionbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from api import views as api_views
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter


router = DefaultRouter()
router.register(r'users', api_views.UserViewSet, 'users')
router.register(r'questions', api_views.QuestionViewSet, basename="questions")
router.register("questions/(?P<question_pk>[^/.]+)/answers", api_views.AnswerViewSet, 'question_answers')
router.register("all_questions/(?P<question_pk>[^/.]+)/all_answers", api_views.AllAnswerViewSet, 'all_question_all_answers')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api-auth/', include('rest_framework.urls')),

    path('api/answers/', api_views.AnswerListRetrieve.as_view({'get': 'list'}), name='answers-list'),
    path('api/answers', api_views.AnswerListRetrieve.as_view({'get': 'list'}), name='answers-list'),
    path('api/answers/<int:pk>/', api_views.AnswerListRetrieve.as_view({'get': 'retrieve', "put": "update", "patch": "partial_update", "delete": "destroy"}), name='answer-detail'),
    path('api/answers/<int:pk>', api_views.AnswerListRetrieve.as_view({'get': 'retrieve', "put": "update", "patch": "partial_update", "delete": "destroy"}), name='answer-detail'),

    path('api/all_questions/', api_views.FavoriteQuestionView.as_view({'get': 'list'}), name='all-questions-list'),
    path('api/all_questions', api_views.FavoriteQuestionView.as_view({'get': 'list'}), name='all-questions-list'),
    path('api/all_questions/<int:pk>/', api_views.FavoriteQuestionView.as_view({'get': 'retrieve'}), name='all-question-detail'),
    path('api/all_questions/<int:pk>', api_views.FavoriteQuestionView.as_view({'get': 'retrieve'}), name='all-question-detail'),

    path('api/favorite_questions/', api_views.FavoriteQuestionView.as_view({'get': 'list'}), name='favorite-questions-list'),
    path('api/favorite_questions', api_views.FavoriteQuestionView.as_view({'get': 'list'}), name='favorite-questions-list'),
    path('api/favorite_questions/<int:pk>/', api_views.FavoriteQuestionView.as_view({'get': 'retrieve'}), name='favorite-question-detail'),
    path('api/favorite_questions/<int:pk>', api_views.FavoriteQuestionView.as_view({'get': 'retrieve'}), name='favorite-question-detail'),

    path('api/favorite_answers/', api_views.FavoriteAnswerView.as_view({'get': 'list'}), name='favorite-answers-list'),
    path('api/favorite_answers', api_views.FavoriteAnswerView.as_view({'get': 'list'}), name='favorite-answers-list'),
    path('api/favorite_answers/<int:pk>/', api_views.FavoriteAnswerView.as_view({'get': 'retrieve'}), name='favorite-answer-detail'),
    path('api/favorite_answers/<int:pk>', api_views.FavoriteAnswerView.as_view({'get': 'retrieve'}), name='favorite-answer-detail'),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
