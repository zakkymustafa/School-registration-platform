from django.contrib import admin
from .models import Teacher
# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
	list_display=("first_name","last_name","Email","date_joined")
	search_fields=("last_name","Email","first_name")

admin.site.register(Teacher,TeacherAdmin)	
	
