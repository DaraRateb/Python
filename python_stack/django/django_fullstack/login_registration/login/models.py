from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        regexalpha=re.compile(r'^[a-zA-Z]+$')
        regexemail=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # add keys and values to errors dictionary for each invalid field
        # if "first_name" in errors.keys():
        if len(postData['first_name']) < 2 or not regexalpha.match(postData['first_name']):
            errors["first_name"] = "User's first name should be at least 2 letters"
        if len(postData['last_name']) < 2 or not regexalpha.match(postData['last_name']):
            errors["last_name"] = "User's last name should be at least 2 letters"
        if postData['password']!=postData['confirm_password']:
            errors["confirm_password"] = "Confirm password must matches the password!"
        if not regexemail.match(postData['email']):
            errors["email"] = "Invalid email address!"
        if len(postData['password'])<8:
            errors['password']= "Password should be at least 8 characters"
        return errors

class Users(models.Model):

    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    password=models.CharField(max_length=45)
    # birthday=models.DateField()
    #we should not add a column for confirmation password in the database
    confirm_password=models.CharField(max_length=45)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects =UserManager()

def create_user(info):
    hashed_password = bcrypt.hashpw(info["password"].encode(), bcrypt.gensalt()).decode()
    Users.objects.create(first_name=info["first_name"],
            last_name=info["last_name"],email=info["email"],password=hashed_password,
            confirm_password=info["confirm_password"])
    return Users.objects.last()
                


def get_user(info):
    return  Users.objects.filter(email=info["email"])

