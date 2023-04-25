from django.db import models
from django.urls import reverse


# Create your models here.
class Student(models.Model):
    reg_no = models.BigIntegerField()
    name = models.CharField(max_length=250)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    dob = models.DateField()
    joined_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.department}"

    def get_absolute_url(self):
        return reverse('students_list')
