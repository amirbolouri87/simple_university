from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from django.utils import timezone
from django import forms
from django.contrib.auth.forms import PasswordChangeForm , PasswordResetForm
# Create your models here.






class Collage(models.Model):
    class Meta:
         verbose_name ="دانشکده"
         verbose_name_plural = "دانشکده"
 

    Collagename = models.CharField(max_length= 30 , verbose_name="نام دانشکده" , )
    def __str__(self):
         return self.Collagename


class Major(models.Model):
    class Meta:
         verbose_name = " رشته تحصیلی"
         verbose_name_plural = " رشته تحصیلی"
   
    MajorName = models.CharField(max_length= 30 , verbose_name="نام رشته")
    collage= models.ForeignKey(Collage , on_delete=models.CASCADE   ,null=True ,  verbose_name="نام دانشکده")

    def __str__(self) :
         return self.MajorName
    



class Lesson(models.Model):
    class Meta :
        verbose_name = "دروس ارايه شده"
        verbose_name_plural = "دروس ارايه شده"


    NameOfLesson = models.CharField(max_length=20 ,verbose_name="نام درس")
    SerialOfLesson =models.IntegerField( unique=True , verbose_name="کد درس")
    Major = models.ForeignKey(Major , on_delete=models.CASCADE , verbose_name="رشته")


    def __str__(self) :
        return self.NameOfLesson



    
class ChoiseLesson(models.Model):
    class Meta:
        verbose_name = "انتخاب واحد"
        verbose_name_plural = "انتخاب واحد"
    
    Namelesson = models.ForeignKey( Lesson, on_delete=models.CASCADE , verbose_name="نام درس" , null=True )
    ClassDayTime =models.DateTimeField(default= datetime, verbose_name="زمان و تاریخ شروع کلاس" , null=True , blank = True)
    ExamDateTime = models.DateTimeField(default=datetime, verbose_name= "  زمان و تاریخ امتحان" , null=True , blank = True)
    

    def __str__(self) :
        return self.Namelesson



class Authticat(models.Model):
    class Meta:
        verbose_name = "احراز هویت"
        verbose_name_plural ="احراز هویت" 
    
    Fullname =models.CharField(max_length=30 , verbose_name="نام و نام خانوادگی")
    Phonenumber = models.IntegerField( verbose_name="شماره همراه")
    Birth =models.DateField(verbose_name="تاریخ تولد")
    


    @property
    
    def permission_Authticat(self , request , username= None , password = None):
        user = User.objects.get(username = username)
        if user.check_password(password):
         
         return user
        
        else :
            User.DoesNotExist
            return None




class Register(models.Model):
    class Meta:
        verbose_name = "ثبت نام"
        verbose_name_plural = "ثبت نام"


       
    Fullname =models.CharField(max_length=30 , verbose_name="نام و نام خانوادگی")
    FatherName = models.CharField(max_length=20 , verbose_name="نام پدر")
    Birth = models.DateField(verbose_name="تاریخ تولد")
    NationalNumber = models.IntegerField(verbose_name="کد ملی")
    Address = models.CharField(max_length=100 , verbose_name="ادرس")
    PostalCode=models.IntegerField( verbose_name="کدپستی")
    Major=models.ForeignKey(Major , on_delete=models.CASCADE ,verbose_name="رشته" )
    CollageName = models.ForeignKey(Collage , on_delete=models.CASCADE , verbose_name="دانشکده")
    Content = models.CharField(max_length=150 , verbose_name= " توضیحات")
    Student_id = models.IntegerField(unique=True , verbose_name="شماره دانشچویی" , null=True ,) 
    user = models.OneToOneField(User, on_delete=models.CASCADE , verbose_name="نام کاربری")
    password = models.CharField(max_length=128 , verbose_name="رمز عبور")


    Grade_choises = (( 1, 'لیسانس')  , ( 2 , 'فوق لیسانس') , ( 3 ,'دکتری'))
    Grade = models.CharField(choices=Grade_choises, verbose_name="مقطع" )

    def __str__(self) :
        return self.Fullname

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))




class Teacher(models.Model):
    class Meta:
        verbose_name = "اساتید"
        verbose_name_plural = "اساتید"



    Fullname =models.CharField(max_length=30 , verbose_name="نام استاد")
    NationalNumber = models.IntegerField(verbose_name="کدملی")
    Major=models.ForeignKey(Major , on_delete=models.CASCADE , verbose_name="رشته")
    Grade_choises = ((2, 'فوق لیسانس') , (3 , 'دکتری'))
    Grade = models.CharField(choices=Grade_choises , verbose_name="مدرک")

    def __str__(self) :
        return self.Fullname
    



class Borrow(models.Model):
    class Meta:
        verbose_name = "امانت"
        verbose_name_plural = "امانت"
    

    borrow_date = models.DateTimeField(default=timezone.now , verbose_name="تحویل گرفتن")
    return_date = models.DateTimeField(null=True, blank=True, verbose_name="تحویل دادن")



    def __str__(self) :
        return self.return_date


class Liberary(models.Model):
    class Meta:
        verbose_name = "کتابخانه"
        verbose_name_plural = "کتابخانه"

    BookName = models.CharField( max_length=30 , verbose_name="نام کتاب")
    Student_id = models.ForeignKey(Register , on_delete=models.CASCADE , verbose_name="شماره دانشجویی")
    grouping = models.ForeignKey(Major , on_delete=models.CASCADE , verbose_name="دسته بندی")
    Writer =models.ForeignKey(Teacher , on_delete=models.CASCADE ,verbose_name="نویسنده" )
    CheckOut = models.OneToOneField(Borrow, on_delete=models.CASCADE , verbose_name="زمان امانت گیری")
    content =models.CharField(max_length=100 , blank=True , verbose_name= "نظر")



    def __str__(self) :
        return self.Student_id

