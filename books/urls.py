from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView,BookAPIListView,BookAPICreateView
from rest_framework import serializers


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('books/',BookAPIListView.as_view()),
    path('bookcreate/', BookAPICreateView.as_view())
]
