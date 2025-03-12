
from django.contrib import admin
from django.urls import path
from users.views import user_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/', user_profile, name='user_profile'),
]
