from django.urls import path
from .views import add_student
from .views import list_students
from .views import student_detail
from .views import edit_student 

urlpatterns=[
    
    path("add/",add_student,name="add_student"),
    path("list/",list_students,name="list_students"),
    path("detail/<int:pk>/",student_detail,name="student_detail"),
    path("edit/<int:pk>/",edit_student,name="edit_student"),
]