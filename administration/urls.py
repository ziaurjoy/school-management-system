from django.urls import path
from . import views

urlpatterns = [
    path('', views.administration, name='administration'),
    path('login', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='user-logout'),
    path('create/employee', views.create_employee, name='create-employee'),


]