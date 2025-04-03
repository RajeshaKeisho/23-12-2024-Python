from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import login, logout
from .models import ProtectedData
from .serializers import (
    ProtectedDataSerializer, 
    UserSerializer, 
    MyTokenObtainPairSerializer,
    RegisterSerializer,
    LoginSerializer
)

class ProtectedDataList(generics.ListCreateAPIView):
    queryset = ProtectedData.objects.all()
    serializer_class = ProtectedDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProtectedDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProtectedData.objects.all()
    serializer_class = ProtectedDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Create DRF Token
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key,
            "message": "User created successfully"
        })

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        
        # DRF Token Authentication
        token, created = Token.objects.get_or_create(user=user)
        
        # JWT Authentication
        refresh = RefreshToken.for_user(user)
              
        login(request, user)
        
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "drf_token": token.key,
            "jwt": {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            },
        })

class LogoutAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # DRF Token logout
        if 'Authorization' in request.headers and 'Token' in request.headers['Authorization']:
            try:
                token_key = request.headers['Authorization'].split(' ')[1]
                token = Token.objects.get(key=token_key)
                token.delete()
            except (Token.DoesNotExist, IndexError):
                pass
        
        # JWT logout (add refresh token to blacklist)
        refresh_token = request.data.get('refresh_token')
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
            except Exception:
                pass
                
        # Session logout
        logout(request)
        
        return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
