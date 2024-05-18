from rest_framework import serializers
from .models import Author, Book ,Category

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields = ['id','name']

class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(many=True, queryset=Author.objects.all())
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())

    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'categories', 'price', 'stock']
