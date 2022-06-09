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

    path('api/all_questions/', api_views.AllQuestionView.as_view({'get': 'list'}), name='all-questions-list'),
    path('api/all_questions', api_views.AllQuestionView.as_view({'get': 'list'}), name='all-questions-list'),
    path('api/all_questions/<int:pk>/', api_views.AllQuestionView.as_view({'get': 'retrieve'}), name='all-question-detail'),
    path('api/all_questions/<int:pk>', api_views.AllQuestionView.as_view({'get': 'retrieve'}), name='all-question-detail'),

    path('api/all_answers/', api_views.AllAnswerView.as_view({'get': 'list'}), name='all-answers-list'),
    path('api/all_answers', api_views.AllAnswerView.as_view({'get': 'list'}), name='all-answers-list'),
    path('api/all_answers/<int:pk>/', api_views.AllAnswerView.as_view({'get': 'retrieve'}), name='all-answer-detail'),
    path('api/all_answers/<int:pk>', api_views.AllAnswerView.as_view({'get': 'retrieve'}), name='all-answer-detail'),

    path('api/all_questions/<int:pk>/favorite', api_views.FavoriteQuestionUpdateView.as_view(), name='favorite-question'),
    path('api/all_questions/<int:pk>/favorite/', api_views.FavoriteQuestionUpdateView.as_view(), name='favorite-question'),

    path('api/all_answers/<int:pk>/favorite', api_views.FavoriteAnswerUpdateView.as_view(), name='favorite-answer'),
    path('api/all_answers/<int:pk>/favorite/', api_views.FavoriteAnswerUpdateView.as_view(), name='favorite-answer'),

    path('api/favorite_questions', api_views.FavoriteQuestionListView.as_view(), name='favorite-answer-detail'),
    path('api/favorite_questions/', api_views.FavoriteQuestionListView.as_view(), name='favorite-answer-detail'),

    path('api/favorite_answers', api_views.FavoriteAnswerListView.as_view(), name='favorite-answer-detail'),
    path('api/favorite_answers/', api_views.FavoriteAnswerListView.as_view(), name='favorite-answer-detail'),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
