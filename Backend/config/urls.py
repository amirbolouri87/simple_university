"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from STU.views import CollageListView ,  MajorListView ,AuthticatListView , RegisterListView ,  BorrowListView , LiberaryListView
from Students.views import MajorListViews , LessonListView , ChoiseLessonView , TeacherListView 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('STU/Borrow/list' , BorrowListView , name = 'borrow_list'),
    path('STU/Collage/lisr' , CollageListView, name='collage_name'),
    path('STU/liberary/list' , LiberaryListView , name='liberary_list'),
    path('STU/Major/list' , MajorListView, name='majors_list'),
    path('STU/Register/list' , RegisterListView , name = 'register_list'),
    path('STU/Authicat/list/', AuthticatListView, name='authticat_list'),
    path('Students/Major/list' , MajorListViews, name='majors_list'),
    path('Students/Lesson/list' , LessonListView , name='lesson_list'),
    path('Students/ChoiseLesson/list' , ChoiseLessonView , name='choiselesson_name'),
    path('Students/Teacher/list' , TeacherListView , name='teacher_list'),
]