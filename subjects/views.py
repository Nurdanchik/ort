from rest_framework import generics, permissions
from . import models
from . import serializers

class SubjectsListAPIView(generics.ListCreateAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]