from django.db import models

# Create your models here.

class TeacherInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    designation = models.CharField(max_length=50)
    phone = models.IntegerField()
    select_gender = (
        ('male','Male'),
        ('female','female')
    )
    gender = models.CharField(choices=select_gender, max_length=10)

    def __str__(self):
        return self.name