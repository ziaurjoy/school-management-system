

from django.urls import path
from . import views

urlpatterns = [
    path('create', views.CreateStudent.as_view(), name = 'create-student'),
    # path('create', views.create_student, name = 'create-student'),

]
