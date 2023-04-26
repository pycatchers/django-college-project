from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Student


# Create your views here.

class StudentsListView(ListView):
    model = Student
    template_name = "students.html"


class StudentDetailView(DetailView):
    model = Student
    template_name = "student_detail.html"


class StudentCreateView(CreateView):
    model = Student
    template_name = "student_create.html"
    fields = "__all__"


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student_delete.html"
    success_url = reverse_lazy('students_list')


class StudentUpdateView(UpdateView):
    model = Student
    template_name = "student_update.html"
    fields = "__all__"
