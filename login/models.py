from django.db import models
from django.contrib.auth.models import AbstractBaseUser
class Token(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=10)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email

class UserModel(AbstractBaseUser):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    date=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField()
    token = models.CharField(max_length=255)
    last_login = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.first_name


    

