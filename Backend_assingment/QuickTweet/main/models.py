from django.db import models
from django_cryptography.fields import encrypt
# Create your models here.

class UserData(models.Model):
    name=models.CharField(max_length=255,blank=True,null=True)
    api_key=encrypt(models.CharField(max_length=1000,blank=True,null=True))
    api_secret=encrypt(models.CharField(max_length=1000,blank=True,null=True))
    access_token=encrypt(models.CharField(max_length=1000,blank=True,null=True))
    access_secret=encrypt(models.CharField(max_length=1000,blank=True,null=True))
    bearer_token=encrypt(models.CharField(max_length=1000,blank=True,null=True))

    def __str__(self):
        return self.name if self.name else "Unnamed User"  

