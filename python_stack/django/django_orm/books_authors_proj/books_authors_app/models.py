from django.db import models


class Author(models.Model):
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    notes = models.CharField(max_length=225)

class Book(models.Model):
    title=models.CharField(max_length=225)
    desc=models.CharField(max_length=225)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    authors = models.ManyToManyField(Author, related_name="books")



# Create your models here.
