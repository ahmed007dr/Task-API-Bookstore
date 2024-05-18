from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ForeignKey(Author, related_name='books',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category, related_name='books')
    stock = models.IntegerField()
    def __str__(self):
        return self.title