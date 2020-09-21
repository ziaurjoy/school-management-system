from django.shortcuts import render
from .models import StudentInfo
from .forms import StudentCreateForm
from django.views import generic


# Create your views here.

class StudentList(generic.ListView):
    model = StudentInfo
    context_object_name = 'students'
    template_name = 'student/list.html'


class CreateStudent(generic.CreateView):
    form_class = StudentCreateForm
    model = StudentInfo
    template_name = 'student/create.html'
    success_url = 'http://localhost:8000/student/list'


class UpdateStudent(generic.UpdateView):
    form_class = StudentCreateForm
    model = StudentInfo
    template_name = 'student/create.html'
    success_url = 'http://localhost:8000/student/list'


class StudentDelete(generic.DeleteView):
    model = StudentInfo
    context_object_name = 'delete_id'
    template_name = 'student/delete.html'
    success_url = 'http://localhost:8000/student/list'


