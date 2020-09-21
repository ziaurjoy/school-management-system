from django.shortcuts import render

# Create your views here.

def administration(request):
    return render(request,'backend/pages/administratioin.html')