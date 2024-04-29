from django.shortcuts import render
from .models import Collage , Major , Lesson, ChoiseLesson , Authticat , Register , Teacher
# Create your views here.
from django.contrib.auth.models import User



def CollageListView(request):
    Collages = Collage

    context = {
        "collage" : Collages
    }

    return render (request , "STU/collage.html", context)




def MajorListView(request):
    Majors = Major

    context = {
        "major" : Majors
    }

    return render(request , "STU/major.html", context)



def LessonListView(request):
    Lessons = Lesson

    context ={
        "lesson" : Lessons

    }
    return render (request ,"STU/lesson.html"  ,context)



def ChoiseLessonView(request):
    ChoiseLessons = ChoiseLesson

    context = {
        "choiselesson" : ChoiseLessons
    }

    return render (request ,"STU/choiselesson.html" , context )




def AuthticatListView(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

    auth = Authticat()

    user = auth.permission_Authticat(request , username , password)


    if user:
            return render(request ,'authenticated.html', {'user' : user})
    elif ():
            return render(request, 'authentication_error.html', {})
    else:
             return render(request, 'authentication_form.html', {})
    


def RegisterListView(request):
     Registers = Register

     context ={
         "Register" : Registers
    }        
     return render (request ,"STU/register.html" , context )


def TeacherListView(request):
     Teachers = Teacher

     context = {
          "Teacher" : Teachers
     }
     return render (request ,"STU/register.html" , context )


