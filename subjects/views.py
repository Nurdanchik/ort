from rest_framework import generics, permissions, status
from . import models
from rest_framework.views import APIView
from . import serializers
from rest_framework.response import Response
from datetime import timezone, timedelta
from django.utils import timezone
from datetime import timedelta


class SubjectsListAPIView(generics.ListAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]

class SubjectTestsAPIView(generics.ListAPIView):
    serializer_class = serializers.TestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        subject_id = self.kwargs['subject_id']
        return models.Test.objects.filter(subject_id=subject_id)

class SubjectTopicsAPIView(generics.ListAPIView):
    serializer_class = serializers.TopicSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        subject_id = self.kwargs['subject_id']
        return models.Topic.objects.filter(subject_id=subject_id)

class TopicQuestionsAPIView(generics.ListAPIView):
    serializer_class = serializers.QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        topic_id = self.kwargs['topic_id']
        return models.Question.objects.filter(topic_id=topic_id)


class StartTestAPIView(APIView):
    def post(self, request, test_id):
        try:
            test = models.Test.objects.get(id=test_id)
        except models.Test.DoesNotExist:
            return Response({"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND)

        # Преобразование test_duration_minutes в секунды
        test_duration_seconds = (test.test_duration_minutes.hour * 3600) + (
                    test.test_duration_minutes.minute * 60) + test.test_duration_minutes.second

        # Получение текущего времени
        start_time = timezone.now()

        # Рассчитываем end_time, добавив к start_time длительность теста
        end_time = start_time + timedelta(seconds=test_duration_seconds)

        # Создаем экземпляр Result с указанием scheduled_end_time
        result = models.Result.objects.create(
            user_id=request.user,
            test_id=test,
            start_time=start_time,
            end_time=end_time,
            scheduled_end_time=end_time  # Указываем scheduled_end_time равным end_time
        )

        # Возвращаем успешный ответ с информацией о созданном результате
        return Response({
            "result_id": result.id,
            "user_id": result.user_id.id,
            "test_id": result.test_id.id,
            "start_time": result.start_time,
            "end_time": result.end_time,
            "scheduled_end_time": result.scheduled_end_time
        }, status=status.HTTP_201_CREATED)