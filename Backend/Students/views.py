from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import  Major , Lesson, ChoiseUnit  ,Teacher




def MajorListViews(request):
    Majors = Major.objects.all()

    context = {
        "major" : Majors
    }

    return render(request , "Students/major.html", context)



def LessonListView(request):
    Lessons = Lesson

    context ={
        "lesson" : Lessons

    }
    return render (request ,"Students/lesson.html"  ,context)



def ChoiseLessonView(request):
    ChoiseLessons = ChoiseUnit.objects.all()

    context = {
        "choiselesson" : ChoiseLessons
    }


    return render (request ,"Students/choiselesson.html" , context )






def TeacherListView(request):
     Teachers = Teacher.objects.all()

     context = {
          "Teacher" : Teachers
     }
     return render (request ,"Students/register.html" , context )




