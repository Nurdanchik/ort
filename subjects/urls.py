from django.urls import path
from .views import SubjectsListAPIView

urlpatterns = [
    path('subjects/', SubjectsListAPIView.as_view(), name='subjects'),
]