from django.shortcuts import render

from .models import StudentInfo
from .forms import StudentCreateForms
# Create your views here.



def create_student(request):
    forms = StudentCreateForms()
    if request.method == 'POST':
        forms = StudentCreateForms(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            age = forms.cleaned_data['age']
            gender = forms.cleaned_data['gender']
            StudentInfo.objects.create(
                name = name,
                age = age,
                gender = gender
            )
    context = {'forms': forms}
    return render(request,'student/create.html',context)
