from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_teacher, name='create-teacher'),
    path('list', views.teacher_list, name='teacher-list'),
    path('update/<int:teacher_id>', views.teacher_update, name='teacher-update'),
    path('delete/<int:teacher_id>', views.teacher_delete, name='teacher-delete'),

]