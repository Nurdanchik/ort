from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegistrationSerializer, LoginSerializer

class RegistrationAPIView(CreateAPIView):
    serializer_class = RegistrationSerializer

class LoginAPIView(TokenObtainPairView):
    serializer_class = LoginSerializer