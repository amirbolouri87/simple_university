from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django_jalali.db import models as jmodels
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
    ClassDayTime =jmodels.jDateTimeField( verbose_name="زمان و تاریخ شروع کلاس" , null=True , blank = True)
    ExamDateTime = jmodels.jDateTimeField( verbose_name= "  زمان و تاریخ امتحان" , null=True , blank = True)
    

    def __str__(self) :
        return self.Namelesson



class Authticat(models.Model):
    class Meta:
        verbose_name = "احراز هویت"
        verbose_name_plural ="احراز هویت" 
    
    Fullname =models.CharField(max_length=30 , verbose_name="نام و نام خانوادگی")
    Phonenumber = models.IntegerField( verbose_name="شماره همراه")
    Birth =jmodels.jDateField(verbose_name="تاریخ تولد")
    


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
    Birth = jmodels.jDateField(verbose_name="تاریخ تولد")
    NationalNumber = models.IntegerField(verbose_name="کد ملی")
    Address = models.CharField(max_length=100 , verbose_name="ادرس")
    PostalCode=models.IntegerField( verbose_name="کدپستی")
    Major=models.ForeignKey(Major , on_delete=models.CASCADE ,verbose_name="رشته" )
    CollageName = models.ForeignKey(Collage , on_delete=models.CASCADE , verbose_name="دانشکده")
    Content = models.CharField(max_length=150 , verbose_name= " توضیحات")
    Student_id = models.IntegerField(unique=True , verbose_name="شماره دانشچویی" , null=True ,) 
    user = models.OneToOneField(User, on_delete=models.CASCADE , verbose_name="نام کاربری" , null=True)
    TermEnteryCode = models.IntegerField(null=True , verbose_name="کد ترم ورودی")

    Mariide_choise = ((1,"مجرد" ) , (2,"متاهل"))
    MarridSituation = models.IntegerField(choices=Mariide_choise , verbose_name= "وضیعت تاهل", null=True)

    email = models.EmailField(unique=True , verbose_name="نامه الکترونیکی" , null=True)
    DataEnrollment = jmodels.jDateField(verbose_name="تاریخ ثیت نام" , null=True)
    DiplomaAvrage =models.DecimalField(decimal_places= 2    , max_digits=2 , verbose_name="معدل دیپلم" , null=True)


    Admission_choises = ((1 , "بدون کنکور") , (2 , "با کنکور" ))
    Admission =models.IntegerField(choices=Admission_choises , verbose_name="نحوه پذیرش" , null=True)

    Gender_choise = (( 1, "زن") , (2 , "مرد"))
    Gender =models.IntegerField(choices=Gender_choise , verbose_name="جنسیت", null=True)

    PlaceOfIssue = models.CharField(null = True , verbose_name="محل صدور")

    choise_eduacationsStatus = ((1 ,"در حال تحصیل") , (2 , "اخراج") , (3,"انصراف") , (4,"مرخصی"))
    EduacatinoalStatus = models.IntegerField(choices=choise_eduacationsStatus , verbose_name="وضیعت تحصیل" , null=True)

    choise_religion = ((1 , "شیعه") , (2 , "سنی") ,(3 , "دیگر") ) 
    Religion = models.IntegerField(choices=choise_religion , verbose_name="مذهب" , null=True)



    Grade_choises = (( 1, 'لیسانس')  , ( 2 , 'فوق لیسانس') , ( 3 ,'دکتری'))
    Grade = models.IntegerField(choices=Grade_choises, verbose_name="مقطع" )

    def __str__(self) :
        return self.Fullname




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
    

    borrow_date = jmodels.jDateTimeField(default=timezone.now , verbose_name="تحویل گرفتن")
    return_date = jmodels.jDateTimeField(null=True, blank=True, verbose_name="تحویل دادن")



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

