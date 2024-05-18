from django.urls import path
from .api import BookDetailView,BookListCreateView,AuthorListView,CategoryListView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
]
