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
    authors = AuthorSerializer(many=True)
    category = CategorySerializer(many=True)
    class Meta:
        model =Book
        fields = ['id','title','authors','price','categories','stock']