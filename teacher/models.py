from turtle import mode
from django.db import models
from school.models import MyUser
from django.urls import reverse

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=100)
    course_code=models.IntegerField(unique=True)
    lecturer=models.OneToOneField(MyUser,on_delete=models.CASCADE)
    course_description=models.CharField(max_length=100)
    duration=models.FloatField(null=True)
    capacity=models.IntegerField(null=True)
    photo=models.ImageField(upload_to="teacher",blank=True)

    def get_lessons(self):
        return self.lesson_set.all()

    def get_absolute_url(self):
        return reverse('teacher:courses')

    
    def __str__(self):
        return self.course_name

class Lesson(models.Model):
    lesson_code=models.CharField(max_length=100,unique=True)
    lesson_number=models.CharField(max_length=50,null=True,unique=True)
    lesson_title=models.CharField(max_length=50,null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    lesson_description=models.CharField(max_length=100)
    video=models.FileField(upload_to="teacher",blank=True)

    def __str__(self):
        return self.lesson_title
