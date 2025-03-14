from django.urls import path
from .views import AuthorListView, AuthorDetailView, PostListView, PostDetailView

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),

    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post-detail'),
]