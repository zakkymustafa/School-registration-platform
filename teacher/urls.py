from django.urls import path
from .views import add_teacher
from .views import list_teachers
from .views import teacher_detail
from .views import edit_teacher

urlpatterns=[
    path("add/",add_teacher,name="add_teacher"),
    path("list/",list_teachers,name="list_teachers"),
    path("detail/<int:pk>/",teacher_detail,name="teacher_detail"),
    path("edit/<int:pk>/",edit_teacher,name="edit_teacher"),
]