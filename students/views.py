from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student


# Create your views here.

class StudentsListView(ListView):
    model = Student
    template_name = "students.html"


class StudentDetailView(DetailView):
    model = Student
    template_name = "student_detail.html"
