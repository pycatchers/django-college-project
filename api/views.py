from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from students.models import Student
from .serializers import StudentSerializer


# Create your views here.
class StudentListCreateApiView(ListCreateAPIView):
    queryset = Student.objects.all()    # gets all rows from the table
    serializer_class = StudentSerializer


class StudentDetailUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
