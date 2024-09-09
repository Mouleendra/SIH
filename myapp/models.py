from django.db import models

# Create your models here.
class User(models.Model):
    Username =  models.CharField(max_length=50)
    Email =  models.EmailField(max_length=50)
    Password =  models.CharField(max_length=50)
    Confirm_Password =  models.CharField(max_length=50)
