from django.urls import path

from students.views import StudentsListView, StudentDetailView, StudentCreateView, StudentDeleteView, StudentUpdateView

urlpatterns = [
    path("students/", StudentsListView.as_view(), name="students_list"),
    path("student/<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
    path("student/create/", StudentCreateView.as_view(), name="student_create"),
    path("student/<int:pk>/delete", StudentDeleteView.as_view(), name="student_delete"),
    path("student/<int:pk>/update", StudentUpdateView.as_view(), name="student_update")
]
