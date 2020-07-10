
from django.db import models

class Registration(models.Model):
    username=models.CharField(max_length=50)
    emailaddress=models.EmailField(max_length=50,primary_key=True)
    password=models.CharField(max_length=20)
class Login(models.Model):
    userid = models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=20)
    usertype=models.CharField(max_length=20)
    objects = models.Manager()
class Feedback(models.Model):
    name= models.CharField(max_length=50)
    emailaddress = models.EmailField(max_length=50,primary_key=True)
    telephone=models.CharField(max_length=15)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=500)

