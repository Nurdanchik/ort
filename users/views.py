from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegistrationSerializer, LoginSerializer, UserInfoSerializer
from rest_framework import generics, permissions
from .models import CustomUser

class RegistrationAPIView(CreateAPIView):
    serializer_class = RegistrationSerializer

class LoginAPIView(TokenObtainPairView):
    serializer_class = LoginSerializer

class UserInfoAPIView(generics.ListAPIView):
    serializer_class = UserInfoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return CustomUser.objects.filter(id=user_id)