from rest_framework import serializers
from . import models


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = ['id', 'subject_name', 'photo', 'description']


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Test
        fields = ['id', 'test_name', 'subject_id', 'test_duration_minutes']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Topic
        fields = ['id', 'topic_name', 'subject_id', 'image', 'description', 'question_type']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = ['id', 'question_text', 'image', 'topic_id']