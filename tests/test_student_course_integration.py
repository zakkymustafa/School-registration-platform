from django.test import TestCase
from student.models import Student
from course.models import Course
from teacher.models import Teacher
import datetime

class StudentCourseTeacherTestCase(TestCase):
	def setUp(self):
		self.student_a = Student.objects.create(first_name='Zakia',
                            last_name='Mustafa',
                            date_of_birth=datetime.date(1996,8,16),
                            registration_number='001254',
                            Email='zakiyamustafazm@gmail.com',
                            place_of_residence='Kilimani',
                            guardian_phone='0728309600',
                            phone_number = '0794231030',
                            id_number = 34292512,
                            date_joined=datetime.date.today()
									)
		self.student_b= Student.objects.create(first_name='Tiffu',
                            last_name='Lalampaa',
                            date_of_birth=datetime.date(2000,7,18),
                            registration_number='001256',
                            Email='jerutotiffany@gmail.com',
                            place_of_residence='Rongai',
                            guardian_phone='0728309622',
                            phone_number = '0794231035',
                            id_number = 39292512,
                            date_joined=datetime.date.today()
									)
		self.python = Course.objects.create(
					 # name='Python',
                     description='subset of Machine Learning',
                     duration_in_months= 10,
                     Course_number='A253'
								)
		self.javascript = Course.objects.create(
					 # name='Javascript',
                     description='all purpose programming language',
                     duration_in_months= 10,
                     Course_number='A254')
		self.electronics = Course.objects.create(
					 # name='Electronics',
                     description='hardware',
                     duration_in_months= 10,
                     Course_number='A255'
									)
		self.teacher_a= Teacher.objects.create(first_name='James',
                    last_name='Mwai',
                    registration_number='001254',
                    Email='jamesmwai@gmail.com',
                    place_of_residence='Lavington',
                    phone_number='0794231930',
                    id_number=24292512,
                    profession='Engineer',
                    date_joined=datetime.date.today()
								)
		self.teacher_b= Teacher.objects.create(first_name='Barre',
                    last_name='Yasin',
                    registration_number='001256',
                    Email='barreyasin@gmail.com',
                    place_of_residence='Lavington',
                    phone_number='0795231930',
                    id_number=24292522,
                    profession='Industrial engineer',
                    date_joined=datetime.date.today()
								)

	def test_student_can_join_many_courses(self):
		self.assertEqual(self.student_a.courses.count(),0)
		self.student_a.courses.add(self.python)
		self.assertEqual(self.student_a.courses.count(),1)
		self.student_a.courses.add(self.javascript)
		self.assertEqual(self.student_a.courses.count(),2)
		self.student_a.courses.add(self.electronics)
		self.assertEqual(self.student_a.courses.count(),3)

	def test_course_can_have_many_students(self):
		self.python.students.add(self.student_a,self.student_b)
		self.assertEqual(self.python.students.count(),2)

	def test_teacher_can_teach_many_courses(self):
		self.teacher_a.courses.add(self.python,self.javascript)
		self.assertEqual(self.teacher_a.courses.count(),2)

	def test_course_can_have_only_one_teacher(self):
		self.python.teacher=self.teacher_a
		self.assertEqual(self.python.teacher.first_name,"James")
		self.electronics.teacher=self.teacher_b
		self.assertEqual(self.electronics.teacher.first_name,"Barre")

	def test_course_teacher_is_in_student_teachers_list(self):
		self.electronics.teacher=self.teacher_b
		self.student_a.courses.add(self.electronics)
		teachers=self.student_a.teachers()
		self.assertTrue(self.teacher_b in teachers)



