from django.urls import path
from .views import add_course
from .views import list_courses
from .views import course_detail
from .views import edit_course

urlpatterns=[
    path("add/",add_course,name="add_course"),
    path("list/",list_courses,name="list_courses"),
    path("detail/<int:pk>/",course_detail,name="course_detail"),
    path("edit/<int:pk>/",edit_course,name="edit_course"),
]