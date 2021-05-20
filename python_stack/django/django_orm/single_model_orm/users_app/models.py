from django.db import models

class Users (models.Model):
    firstname=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email_address=models.CharField(max_length=60)
    age=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
# Create your models here.


