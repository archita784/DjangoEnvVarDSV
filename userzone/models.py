from django.db import models

# Create your models here.
class Feedback(models.Model):
    name= models.CharField(max_length=50)
    emailaddress = models.EmailField(max_length=50,primary_key=True)
    telephone=models.CharField(max_length=15)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=500)