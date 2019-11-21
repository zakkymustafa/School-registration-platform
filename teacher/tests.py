from django.test import TestCase
from .models import Teacher
import datetime
from .forms import TeacherForm
from django.urls import reverse
from django.test import Client

client=Client()

# Create your tests here.

class CreateTeacherTestCase(TestCase):
    def setUp(self):
        self.data = {'first_name':'zakia',
                    'last_name':'Mustafa',
                    'registration_number':'001254',
                    'Email':'zakiyamustafazm@gmail.com',
                    'place_of_residence':'Kilimani',
                    'phone_number':'0794231030',
                    'id_number':34292512,
                    'profession':'Data scientist',
                    'date_joined':datetime.date.today()}
        self.bad_data = {'first_name':'zakia',
                         'last_name':'',
                         'registration_number':'001254',
                         'Email':'',
                         'place_of_residence':'',
                         'id_number':34292512,
                         'date_joined':datetime.date.today()}
    
    def test_teacher_form_accepts_valid_data(self):
        form = TeacherForm(self.data)
        self.assertTrue(form.is_valid())      

    def test_teacher_form_rejects_invalid_data(self):
        form = TeacherForm(self.bad_data)
        self.assertFalse(form.is_valid())

    def test_add_teacher_view(self):
        url=reverse("add_teacher")
        request = client.post(url,self.data)
        self.assertEqual(request.status_code,200)

    def test_add_teacher_bad_view(self):
        
        url=reverse("add_teacher")
        request =client.post(url,self.bad_data)
        self.assertEqual(request.status_code,400)
