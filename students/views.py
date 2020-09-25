from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import StudentInfo, StudentDetailsInfo
from .forms import StudentRegisterationForm
from django.views import generic


# Create your views here.

class StudentList(LoginRequiredMixin,generic.ListView):
    model = StudentInfo
    context_object_name = 'students'
    template_name = 'backend/pages/students/list.html'



def CreateStudent(request):
    forms = StudentRegisterationForm()
    if request.method == "POST":
        forms = StudentRegisterationForm(request.POST)
        if forms.is_valid():
            roll = forms.cleaned_data['roll']
            english_name = forms.cleaned_data['english_name']
            banglali_name = forms.cleaned_data['banglali_name']
            father_name = forms.cleaned_data['father_name']
            mother_name = forms.cleaned_data['mother_name']
            present_address = forms.cleaned_data['present_address']
            permanet_address = forms.cleaned_data['permanet_address']
            date_of_brith = forms.cleaned_data['date_of_brith']
            gender = forms.cleaned_data['gender']


            student_class = forms.cleaned_data['student_class']
            student_shift = forms.cleaned_data['student_shift']
            student_section = forms.cleaned_data['student_section']
            student_session = forms.cleaned_data['student_session']

            std_obj = StudentInfo.objects.create(
                roll = roll,
                english_name = english_name,
                Bangla_name = banglali_name,
                father_name = father_name,
                mother_name = mother_name,
                present_address = present_address,
                permanet_address = permanet_address,
                date_of_brith = date_of_brith,
                gender = gender,
            )
            StudentDetailsInfo.objects.create(
                student = std_obj,
                student_class = student_class,
                student_shift = student_shift,
                student_section = student_section,
                student_session = student_session,

            )
    context = {'forms': forms}
    return render(request,'backend/pages/students/create.html',context)

# class CreateStudent(LoginRequiredMixin,generic.CreateView):
#     form_class = StudentCreateForm
#     model = StudentInfo
#     template_name = 'backend/pages/students/create.html'
#     success_url = 'http://localhost:8000/student/list'



# class UpdateStudent(LoginRequiredMixin,generic.UpdateView):
#     form_class = StudentCreateForm
#     model = StudentInfo
#     template_name = 'backend/pages/students/create.html'
#     success_url = 'http://localhost:8000/student/list'



class StudentDelete(LoginRequiredMixin,generic.DeleteView):
    model = StudentInfo
    context_object_name = 'delete_id'
    template_name = 'backend/pages/students/delete.html'
    success_url = 'http://localhost:8000/student/list'


