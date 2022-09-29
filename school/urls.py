
from django.urls import path
from .import views 

app_name = "school"
urlpatterns=[
    path('home',views.Home.as_view(),name='index'),
    path('about',views.About.as_view(),name='about'),
    path('contact',views.Contacts.as_view(),name='contact'),
    path('course',views.CourseView.as_view(),name='course'),
    path('team',views.Team.as_view(),name='team'),
    path('register',views.RegisterStudentView.as_view(),name='register'),
    path('login',views.LoginView.as_view(),name='login'),
    path('logout',views.LogoutView.as_view(),name='logout'),
    path('lessons/<str:pk>',views.LessonView.as_view(),name="lesson"),
] 