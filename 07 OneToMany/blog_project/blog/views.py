from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author, Post
# Create your views here.

class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'author_list'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'