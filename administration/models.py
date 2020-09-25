from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    phone = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    choise_designation = (
        ('account', 'Account'),
        ('teacher', 'Teacher'),
    )
    designation = models.CharField(choices=choise_designation, max_length=50)
    choise_gender = (
        ('male','Male'),
        ('female','Female'),
    )
    gender = models.CharField(choices=choise_gender,max_length=10)

    def __str__(self):
        return self.name