from django.urls import path
from .views import LoginAPIView, RegistrationAPIView, UserInfoAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('users/<int:user_id>/subscription/', UserInfoAPIView.as_view(), name='profile'),
]