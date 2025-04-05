from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.contrib import admin
from delivery.views import RestaurantViewSet, MenuItemViewSet, CustomerViewSet, OrderViewSet


router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menu-items', MenuItemViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('api/', include(router.urls)),  
]