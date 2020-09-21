

from django.urls import path
from . import views

urlpatterns = [
    path('create', views.CreateStudent.as_view(), name = 'create-student'),
    path('list', views.StudentList.as_view(), name = 'student-list'),
    path('update/<int:pk>', views.UpdateStudent.as_view(), name = 'student-update'),
    path('delete/<int:pk>', views.StudentDelete.as_view(), name = 'student-delete'),

]
