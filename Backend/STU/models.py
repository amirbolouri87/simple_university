from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
# Create your models here.






class Collage(models.Model):
    class Meta:
         verbose_name ="دانشکده"
         verbose_name_plural = "دانشکده"
 

    Collagename = models.CharField(max_length= 30 , verbose_name="نام دانشکده")

    def __str__(self):
         return self.Collagename


class Major(models.Model):
    class Meta:
         verbose_name = " رشته تحصیلی"
         verbose_name_plural = " رشته تحصیلی"
   
    MajorName = models.CharField(max_length= 30 , verbose_name="نام رشته")
    collage = models.ForeignKey(Collage , on_delete=models.CASCADE , related_name='majors'  , verbose_name="نام دانشکده")

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
    
    Namelesson = models.ForeignKey( Lesson, on_delete=models.CASCADE , verbose_name="نام درس" )
    ClassDayTime =models.DateTimeField(default= datetime.date, verbose_name="زمان و تاریخ شروع کلاس" , null=True , blank = True)
    ExamDateTime = models.DateTimeField(default=datetime.date , verbose_name= "  زمان و تاریخ امتحان" , null=True , blank = True)



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
    CollageName = models.ForeignKey(Collage , on_delete=models.CASCADE , verbose_name="دانشکدع")
    Content = models.CharField(max_length=150 , verbose_name= " توضیحات")


    Grade_choises = (( 1, 'لیسانس')  , ( 2 , 'فوق لیسانس') , ( 3 ,'دکتری'))
    Grade = models.CharField(choices=Grade_choises, verbose_name="مقطع" , max_length=1)


    def __str__(self) :
        return self.Fullname


class Teacher(models.Model):
    class Meta:
        verbose_name = "اساتید"
        verbose_name_plural = "اساتید"



    Fullname =models.CharField(max_length=30 , verbose_name="نام استاد")
    NationalNumber = models.IntegerField(verbose_name="کدملی")
    Major=models.ForeignKey(Major , on_delete=models.CASCADE , verbose_name="رشته")
    Grade_choises = ((1 , 'فوق لیسانس') , (2 , 'دکتری'))
    Grade = models.CharField(choices=Grade_choises , verbose_name="مدرک" , max_length=1)


    def __str__(self) :
        return self.Fullname
