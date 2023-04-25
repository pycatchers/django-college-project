from django.urls import path

from api.views import StudentListCreateApiView, StudentDetailUpdateDeleteApiView

urlpatterns = [
    path("students/", StudentListCreateApiView.as_view(), name="students_create_list_api"),
    path("student/<int:pk>", StudentDetailUpdateDeleteApiView.as_view(), name="student_detail_update_delete_api"),
]
