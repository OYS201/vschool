from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from teacher.forms import CourseForm

from django.urls import reverse_lazy
from django.urls import reverse
# Create your views here.
from re import template
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.views.generic import View
from school.models   import MyUser
from teacher.models import Course,Lesson
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from teacher.dec import staff_only
from django.utils.decorators import method_decorator

# Create your views here.



class RegisterTeacherView(View):
    template_name="teacher/create_teacher.html"
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
        index = request.POST.get("index")


        if password != repeat_password:
            messages.add_message(request, messages.ERROR,
                                 "Passwords do not match.")
            return redirect("teacher:register")

        elif MyUser.objects.filter(phone=phone).exists():
            messages.error(request, 'Phone number already exists.')
            return redirect(request.META.get("HTTP_REFERER"))
            
           
               
               
        else:
            teacher = MyUser.objects.create(
               first_name=first_name,last_name=last_name,
               phone=phone,photo=photo,address=address, 
               email=email,index_number=index
            )
            teacher.photo = request.FILES.get('photo')
            teacher.is_staff=True
            teacher.is_superuser=True
            teacher.set_password(password)
           
            teacher.save()
            return redirect("school:index")

       
class LoginView(View):
    template_name = "teacher/login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email_address")
        password = request.POST.get("password")

        user = authenticate(email=email, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            redirect_url = "school:index"
            return redirect(redirect_url)
        else:
            messages.add_message(request, messages.ERROR,
                                 "Invalid credentials")
            return render(request, self.template_name)


class TeachersView(View):
    template_name="teacher/teachersview.html"

    @method_decorator(staff_only())
    def get(self, request, *args, **kwargs):
        context={"teachers":MyUser.objects.all()}
        return render(request,self.template_name,context)


class TeachersDetailsView(View):
    template_name="teacher/profile.html"

    @method_decorator(staff_only())
    def get(self, request,pk,*args, **kwargs):
        teachers=get_object_or_404(MyUser,index_number=pk)
        context={"profile":teachers}
        return render(request,self.template_name,context)


class CourseView(View):
    template_name="teacher/courselist.html"

    @method_decorator(staff_only())
    def get(self, request,*args, **kwargs):
        context={'course':Course.objects.all()}
        return render(request,self.template_name,context)


class UpdateCourseView(UpdateView):
    model = Course
    # fields = ['course_name','course_code','course_name','lecturer','course_description','duration','capacity','photo']
    template_name = 'teacher/update.html'
    form_class=CourseForm

    @method_decorator(staff_only())
    def get_absolute_url(self):
        return reverse('courses')
     

#    , args=[str(self.id)]



    
    

       
        
        
        

        


class CreateCourseView(View):
    template_name="teacher/create_course.html"

    @method_decorator(staff_only())
    def get(self,request):
        context={"myuser":MyUser.objects.all()}
        return render(request,self.template_name,context)

    @method_decorator(staff_only())
    def post(self, request, *args, **kwargs):
        # photo = request.FILES.get("photo")
        lecturer= request.POST.get("lecturer")
        course_name = request.POST.get("name")
        course_code = request.POST.get("code")
        capacity=request.POST.get("capacity")
        duration=request.POST.get("duration")
        description=request.POST.get("duration")
        myuser_object=MyUser.objects.get(first_name=lecturer)

        if Course.objects.filter(course_code=course_code).exists():
            messages.error(request, 'course_code already exists.')
            return redirect(request.META.get("HTTP_REFERER"))
        

        else:
            teacher = Course.objects.create(
            course_name=course_name,course_code=course_code,
            lecturer=myuser_object,
            course_description=description,duration=duration,
            capacity=capacity
            )
        teacher.photo=request.FILES.get('photo')
        teacher.save()
        return redirect("school:course")


class CreateLessonView(View):
    template_name="teacher/createlesson.html"
    @method_decorator(staff_only())
    def get(self,request,*args, **kwargs):
        context={"course":Course.objects.all()}
        return render(request,self.template_name,context)

    @method_decorator(staff_only())
    def post(self, request, *args, **kwargs):
        courselesson=request.POST.get("course")
        lesson_code= request.POST.get('code')
        lesson_number= request.POST.get("number")
        lesson_title = request.POST.get("title")
        lesson_description=request.POST.get("description")
        video=request.POST.get('video')
        mycourse_object=Course.objects.get(course_name=courselesson)

        if Lesson.objects.filter(lesson_code=lesson_code).exists():
            messages.error(request, 'course_code  already exists.')
            return redirect(request.META.get("HTTP_REFERER"))

        elif Lesson.objects.filter(lesson_number=lesson_number).exists():
            messages.error(request, 'number already exists.')
            return redirect(request.META.get("HTTP_REFERER"))
        

        else:
            lesson = Lesson.objects.create(
            lesson_code=lesson_code,lesson_number=lesson_number,
            lesson_title=lesson_title,course=mycourse_object,lesson_description=lesson_description,
            video=video
            )
        lesson.video=request.FILES.get('video')
        lesson.save()
        return redirect("school:course")
        


class LessonView(View):
    template_name="teacher/lesson.html"

    @method_decorator(staff_only())
    def get(self,request,*args, **kwargs):
        lesson=get_object_or_404(Course,course_name=kwargs['pk']).get_lessons()
        context={"lesson":lesson}
        return render(request,self.template_name,context) 


class LessonDetailView(View):
    template_name="teacher/index.html"

    @method_decorator(staff_only())
    def get(self,request,*args, **kwargs):
        lesson=get_object_or_404(Lesson,lesson_title=kwargs['pk'])
        context={"lesson":lesson,"other":Lesson.objects.all()}
        return render(request,self.template_name,context) 


class DeleteCourseView(DeleteView):
    model = Course
    template_name = 'teacher/deletecourse.html'
    success_url = reverse_lazy('teacher:courses')

class UpdateLessonView(UpdateView):
    model = Lesson
    template_name = 'teacher/updatelesson.html'
    form_class=CourseForm

    @method_decorator(staff_only())
    def get_absolute_url(self):
        return reverse('teacher:teachers')

class DeleteLessonView(DeleteView):
    model = Lesson
    template_name = 'teacher/deletelesson.html'
    success_url = reverse_lazy('teacher:courses')

  
        
       







    



