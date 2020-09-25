from django.db import models

# Create your models here.


class StudentShiftInfo(models.Model):
    shift_name = models.CharField(max_length=10)

    def __str__(self):
        return self.shift_name

class StudentClassInfo(models.Model):
    class_name = models.CharField(max_length=20)
    class_short_name = models.CharField(max_length=10)

    def __str__(self):
        return self.class_name


class StudentInfo(models.Model):
    roll = models.IntegerField()
    english_name = models.CharField(max_length=50)
    Bangla_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    present_address = models.TextField()
    permanet_address = models.TextField()
    date_of_brith = models.DateField()
    choise_gender = (
        ('male', 'Male'),
        ('female','Female'),
    )
    gender = models.CharField(choices=choise_gender, max_length=10)

    def __str__(self):
        return self.english_name


class StudentDetailsInfo(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    student_class = models.ForeignKey(StudentClassInfo, on_delete=models.CASCADE)
    student_shift = models.ForeignKey(StudentShiftInfo, on_delete=models.CASCADE)
    student_section = models.CharField(max_length=20,blank=True,null=True)
    student_session = models.IntegerField()

    def __str__(self):
        return self.student_section

