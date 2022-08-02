from django.db import models

class Signup(models.Model):
    User_name=models.CharField(max_length=50)
    Full_name=models.CharField(max_length=50)
    Email_Id=models.EmailField()
    password=models.CharField(max_length=50)