from django.shortcuts import render, redirect

# Create your views here.
from teachers.forms import TeacherCreateForm
from teachers.models import TeacherInfo


def teacher_list(request):
    teachers = TeacherInfo.objects.all()
    context = {'teachers': teachers}
    return render(request,'teachers/list.html',context)


def create_teacher(request):
    forms = TeacherCreateForm()
    if request.method == 'POST':
        forms = TeacherCreateForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('teacher-list')
    context = {'forms': forms}
    return render(request,'teachers/create.html',context)


def teacher_update(request,teacher_id):
    teacher = TeacherInfo.objects.get(id = teacher_id)
    forms = TeacherCreateForm(instance=teacher)
    if request.method == "POST":
        forms = TeacherCreateForm(request.POST,instance=teacher)
        if forms.is_valid():
            forms.save()
            return redirect('teacher-list')
    context = {'forms': forms}
    return render(request,'teachers/create.html',context)


def teacher_delete(request,teacher_id):
    teacher = TeacherInfo.objects.get(id = teacher_id)
    teacher.delete()
    return redirect('teacher-list')