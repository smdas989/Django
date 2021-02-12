from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class CustomStudentModel(AbstractUser):
    standard = models.IntegerField(null=True,blank=True)
    age = models.CharField(max_length=2, null=True)
    gender = models.CharField(max_length=6,null=True)
    roll_no = models.IntegerField(null=True)

   

    

    
