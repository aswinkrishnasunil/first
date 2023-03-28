from django.db import models

# Create your models here.

class table(models.Model):
    fname=models.CharField(max_length=200,null=True)
    lname=models.CharField(max_length=200,null=True)
    gender =  models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
