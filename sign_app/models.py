from django.db import models

# Create your models here.
class UserModel(models.Model):
    username=models.CharField(max_length=20,blank=False)
    passwd=models.CharField(max_length=20,blank=False)