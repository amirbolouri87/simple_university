from django.shortcuts import render
from .models import Collage , Major , Authticat , Register , Borrow , Liberary
# Create your views here.
from django.contrib.auth.models import User



def CollageListView(request):
    Collages = Collage.objects.all()

    context = {
        "collage" : Collages
    }

    return render (request , "STU/collage.html", context)


def MajorListView(request):
    majors = Major.objects.all()

    majors = Major.objects.all()
    return render(request, 'majors.html', {'majors': majors})   




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
     Registers = Register.objects.all()

     context ={
         "Register" : Registers
    }        
     return render (request ,"STU/register.html" , context )





def BorrowListView(request):
     Borrows = Borrow.objects.all()

     context = {
          "Borrow" : Borrows
     }

     return render (request ,"STU/borrow.html" , context)



def LiberaryListView(request):
     Liberarys = Liberary.objects.all()

     context = {
          "Library " :Liberarys
     }


     return render (request , "STU/liberary.html" , context)