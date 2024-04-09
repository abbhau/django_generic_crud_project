from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import Student
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
# Create your views here.


class StudentList(ListView):
    model = Student
    template_name = 'stu_app/student_list.html'


class StudentCreate(CreateView):
    model  = Student
    template_name = 'stu_app/student_form.html'
    fields='__all__'
    success_url = '/p1/students/'


class StudentUpdate(UpdateView):
    model  = Student
    template_name = 'stu_app/student_form.html'
    fields='__all__'
    success_url = '/p1/students/'


class StudentDelete(DeleteView):
    model  = Student
    template_name = 'stu_app/student_confirm_delete.html'
    success_url = '/p1/students/'


class StudentRegister(CreateView):
    model = Student
    template_name = 'stu_app/student_form.html'
    form_class = UserCreationForm
    success_url = '/p1/login/'
