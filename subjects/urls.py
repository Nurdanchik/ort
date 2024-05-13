from django.urls import path
from .views import SubjectsListAPIView, SubjectTestsAPIView, SubjectTopicsAPIView, TopicQuestionsAPIView, StartTestAPIView

urlpatterns = [
    path('subjects/', SubjectsListAPIView.as_view(), name='subjects'),
    path('subjects/<int:subject_id>/tests/', SubjectTestsAPIView.as_view(), name='tests_of_subject'),
    path('subjects/<int:subject_id>/topics/', SubjectTopicsAPIView.as_view(), name='topics_of_subject'),
    path('topics/<int:topic_id>/questions/', TopicQuestionsAPIView.as_view(), name='questions_of_topic'),
    path('tests/<int:test_id>/start/', StartTestAPIView.as_view(), name='open_test'),
]