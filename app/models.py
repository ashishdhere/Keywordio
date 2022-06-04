from django.db import models

# Create your models here.
class Books(models.Model):
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_price = models.IntegerField()
    book_category = models.CharField(max_length=100)
    
class User(models.Model):
    Name = models.CharField(max_length=100)
    email = models.EmailField()
    Password = models.CharField(max_length=100)
    