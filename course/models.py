from django.db import models
from teacher.models import Teacher

# Create your models here.
    
class Course(models.Model):
    name=models.CharField(max_length=50)
    duration_in_months=models.SmallIntegerField()
    Course_number=models.CharField(max_length=50)
    description=models.TextField()
    teacher=models.ForeignKey(Teacher, on_delete=models.PROTECT,null=True,blank=True,related_name='courses')
    image=models.FileField(upload_to="images/",blank=True,null=True)
    def __str__(self):
        return self.name
        
    def name(self):
        return "{} {}".format(self.name)
    
        