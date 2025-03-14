from django.urls import path 
from . import views 

urlpatterns = [
    path('files/', views.file_list, name='file_list'),
    path('files/create/', views.create_file, name='create_file'),
    path('files/download/<int:file_id>/', views.download_file, name='download_file'),
]