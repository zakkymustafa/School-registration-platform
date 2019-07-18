from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	list_display= ("first_name","last_name","registration_number","Email","date_joined","image")
	search_fields=("registration_number","Email","last_name")
	list_filter=("date_joined","date_of_birth")

admin.site.register(Student,StudentAdmin)	


	

