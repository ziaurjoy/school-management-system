from django.contrib import admin
from .models import StudentInfo,StudentShiftInfo,StudentClassInfo,StudentDetailsInfo
# Register your models here.

admin.site.register(StudentShiftInfo)
admin.site.register(StudentClassInfo)
admin.site.register(StudentInfo)
admin.site.register(StudentDetailsInfo)
