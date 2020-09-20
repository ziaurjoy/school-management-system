from django.db import models

# Create your models here.


class StudentInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    choise_gender = (
        ('male', 'Male'),
        ('female','Female'),
        ('other','Other')
    )
    gender = models.CharField(choices=choise_gender, max_length=10)

    def __str__(self):
        return self.name