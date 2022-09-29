from django import forms
from django.forms import ModelForm, TextInput, EmailInput

from teacher.models import Course

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'course_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'course_code': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Code'
                }),
            'course_description': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Code'
                }),
            'capacity': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Code'
                }),
            'duration': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Code'
                })
        }

class UPDATE_LESSON(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'course_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'course_code': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Code'
                }),
            'course_description': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Code'
                }),
            'capacity': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Code'
                }),
            'duration': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Code'
                })
        }