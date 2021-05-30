from django.db import models


class Author(models.Model):
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    notes = models.CharField(max_length=225)

class Book(models.Model):
    title=models.CharField(max_length=225)
    description=models.CharField(max_length=225)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    authors = models.ManyToManyField(Author, related_name="books")



# Create your models here.
def add_book(info):
    Book.objects.create(title=info["title"],description=info["description"])
    return Book.objects.all()
                
def add_author(info):
    Author.objects.create(first_name=info["first_name"],
    last_name=info["last_name"],notes=info["notes"])
    return Author.objects.all()