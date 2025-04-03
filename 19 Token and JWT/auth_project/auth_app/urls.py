from django.urls import path
from .views import (
    ProtectedDataList,
    ProtectedDataDetail,
    MyTokenObtainPairView,
    RegisterAPI,
    LoginAPI,
    LogoutAPI
)

urlpatterns = [
    path('data/', ProtectedDataList.as_view(), name='protected-data-list'),
    path('data/<int:pk>/', ProtectedDataDetail.as_view(), name='protected-data-detail'),
    
    # Authentication URLs
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', LogoutAPI.as_view(), name='logout'),
    
    # JWT URLs
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', MyTokenObtainPairView.as_view(), name='token_refresh'),
]
