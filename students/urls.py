from django.urls import path

from students.views import StudentsListView, StudentDetailView

urlpatterns = [
    path("students/", StudentsListView.as_view(), name="students_list"),
    path("student/<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
]
