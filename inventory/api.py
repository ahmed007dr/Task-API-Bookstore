from rest_framework import generics ,filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book,Category,Author
from .serializer import AuthorSerializer,CategorySerializer,BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filter_filed = ['author__name','categories__name','price','stock']
    ordering_fields = ['title','price','stock']


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer