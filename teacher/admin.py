from django.contrib import admin

from teacher.models import Course, Lesson

# Register your models here.
admin.site.register(Course)
admin.site.register(Lesson)