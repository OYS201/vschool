
from django.urls import path
from .import views 

app_name = "teacher"
urlpatterns=[
    path('register',views.RegisterTeacherView.as_view(),name='register'),
    path('login',views.LoginView.as_view(),name='login'),
    path('teachers',views.TeachersView.as_view(),name='teachersview'),
    path('createcourse',views.CreateCourseView.as_view(),name='createcourse'),
    path('profile/<str:pk>',views.TeachersDetailsView.as_view(),name="profile"),
    path('createlesson',views.CreateLessonView.as_view(),name="createlesson"),
    path('lessons/<str:pk>',views.LessonView.as_view(),name="lessons"),
    path('lessondetails/<str:pk>',views.LessonDetailView.as_view(),name="lessondetails"),
    path('courses',views.CourseView.as_view(),name="courses"),
    path('update/<str:pk>',views.UpdateCourseView.as_view(),name="update"),
    path('deletecourse/<str:pk>',views.DeleteCourseView.as_view(),name="deletecourse"),
    path('updatelesson/<str:pk>',views.UpdateLessonView.as_view(),name="updatelesson"),
    path('deletelesson/<str:pk>',views.DeleteLessonView.as_view(),name="deletelesson"),
    # path('logout',views.LogoutView.as_view(),name='logout'),
] 