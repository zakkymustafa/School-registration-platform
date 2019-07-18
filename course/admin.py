from django.contrib import admin
from .models import Course

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display=("name","Course_number","teacher","description")
    search_fields=("name","description","teacher__first_name","teacher__Email")
    list_filter=("teacher__first_name",)

    

admin.site.register(Course,CourseAdmin)