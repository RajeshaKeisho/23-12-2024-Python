from django.urls import path
from . import views

urlpatterns = [
    # path('api/books/', views.BookListViewPageNumber.as_view(), name='book-list-api-page-number'),
    # path('api/books2/', views.BookListViewLimitOffset.as_view(), name='book-list-api-limit-offset'),
    # path('api/books3/', views.BookListViewCursor.as_view(), name='book-list-api-cursor'),
    

    path('books/', views.BookListViewPageNumber.as_view(), name='book-list-page-number'),
    path('books2/', views.BookListViewLimitOffset.as_view(), name='book-list-limit-offset'),
    path('books3/', views.BookListViewCursor.as_view(), name='book-list-cursor'),
]





