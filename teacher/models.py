from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    place_of_residence=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    id_number=models.IntegerField()
    profession=models.CharField(max_length = 50)
    registration_number=models.CharField(max_length = 50)
    date_joined=models.DateField()
    image=models.FileField(upload_to="image/",blank=True)
    def __str__(self):
        return self.first_name + " " + self.last_name

        
