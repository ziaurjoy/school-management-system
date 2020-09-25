from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from administration.forms import UserLoginForm, EmployeeCreateForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def create_employee(request):
    forms = EmployeeCreateForm()
    if request.method == 'POST':
        forms = EmployeeCreateForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user_obj = User.objects.create(username=username, password=password)
            new_user = forms.save(commit=False)
            new_user.user = user_obj
            new_user.save()
            return redirect('user_login')
    context = {'forms': forms}
    return render(request,'backend/pages/administration/create_employee.html',context)


def user_login(request):
    forms = UserLoginForm()
    if request.method == 'POST':
        forms = UserLoginForm(request.POST)
        if forms.is_valid():
            user = authenticate(
                username = forms.cleaned_data['username'],
                password = forms.cleaned_data['password']
            )
            if user:
                login(request,user)
                return redirect('administration')
    context = {'forms': forms}
    return render(request,'backend/pages/administration/login.html',context)

def user_logout(request):
    logout(request)
    return redirect('user_login')


@login_required()
def administration(request):
    return render(request,'backend/pages/administration/administration.html')
