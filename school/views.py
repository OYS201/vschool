from re import template
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.views.generic import View
from school.models   import MyUser,Contact
from teacher.models import Course
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from teacher.dec import students_only
from django.utils.decorators import method_decorator
from teacher.models import Lesson
# Create your views here.


class Home(View):
    template_name="school/index.html"
    def get(self,request):
        context={"myuser":MyUser.objects.all(),"teach":MyUser.objects.all()}
        return render(request,self.template_name,context)

class About(View):
    template_name="school/about.html"
    def get(self,request):
        return render(request,self.template_name)
        
class Contacts(View):
    template_name="school/contact.html"
    def get(self,request):
        return render(request,self.template_name)

    def post(self,request,*args,**kwargs):
        name=request.POST.get('Name')
        subject=request.POST.get('Subject')
        email=request.POST.get('Email')
        message=request.POST.get('Message')

        contact=Contact.objects.create(
            name=name,subject=subject,message=message,email=email
        )
        contact.save()
        return redirect(request.META.get("HTTP_REFERER"))

class CourseView(View):
    template_name="school/courses.html"
    def get(self,request):
        context={"course":Course.objects.all(),"lesson":Lesson.objects.all()}
        return render(request,self.template_name,context)

class Team(View):
    template_name="school/team.html"
    def get(self,request):
        context={"teach":MyUser.objects.all()}
        return render(request,self.template_name,context)


class RegisterStudentView(View):
    template_name="school/register.html"
    def get(self,request):
        return render(request,self.template_name)

    def post(self, request, *args, **kwargs):
        # photo = request.FILES.get("photo")
        email= request.POST.get("email_address")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone=request.POST.get("phone")
        photo = request.POST.get("photo")
        address = request.POST.get("address")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")

        if password != repeat_password:
            messages.add_message(request, messages.ERROR,
                                 "Passwords do not match.")
            return redirect("school:register")
        else:
            student = MyUser.objects.create(
               first_name=first_name,last_name=last_name,
               phone=phone,photo=photo,address=address, 
               email=email
            )
            student.is_student=True
            student.set_password(password)
           
            student.save()
        return redirect("school:index")

class LoginView(View):
    template_name = "school/login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email_address")
        password = request.POST.get("password")

        user = authenticate(email=email, password=password)

        if user is not None and user.is_student:
            login(request, user)
            redirect_url = "school:index"
            return redirect(redirect_url)
        else:
            messages.add_message(request, messages.ERROR,
                                 "Invalid credentials")
            return render(request, self.template_name)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("school:index")


class LessonView(View):
    template_name="school/lesson.html"

    @method_decorator(students_only())
    def get(self,request,*args, **kwargs):
        lesson=get_object_or_404(Course,course_name=kwargs['pk']).get_lessons()
        context={"lesson":lesson}
        return render(request,self.template_name,context)



    



