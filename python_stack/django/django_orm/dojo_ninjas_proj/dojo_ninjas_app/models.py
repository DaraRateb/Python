from django.db import models
class Dojo(models.Model):
    name=models.CharField(max_length=45)
    city=models.CharField(max_length=45)
    state=models.CharField(max_length=45)
    desc=models.CharField(max_length=45)
    #list => ninja 
# Create your models here.
class Ninjas(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    dojokey = models.ForeignKey(Dojo, related_name="ninja", on_delete = models.CASCADE)

# Create your models here.
