from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField(default="")
    books = models.ManyToManyField(Book,related_name="authors")
    