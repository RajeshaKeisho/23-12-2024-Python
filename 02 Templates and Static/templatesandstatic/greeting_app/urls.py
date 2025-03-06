from django.urls import path 
from . import views

urlpatterns = [
    # path('greet/', views.wish, name='wish'),
    path('wish1/', views.wish1, name='wish1'),
    path('greet/', views.greet, name='greet'),
]