from django.db import models
from django.utils import timezone
# Create your models here.
from django_jalali.db import models as jmodels



class Major(models.Model):
    class Meta:
         verbose_name = " رشته تحصیلی"
         verbose_name_plural = " رشته تحصیلی"
   
    MajorName = models.CharField(max_length= 30 , verbose_name="نام رشته")
    collage= models.CharField(null=True ,  verbose_name="نام دانشکده")

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




class ChoiseUnit(models.Model):
    class Meta:
        verbose_name = "انتخاب واحد"
        verbose_name_plural = "انتخاب واحد"

    id = models.AutoField(primary_key=True)
    Namelesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    ClassDayTime = models.DateTimeField(verbose_name="زمان و تاریخ شروع کلاس", null=True, blank=True)
    ExamDateTime = models.DateTimeField(verbose_name="  زمان و تاریخ امتحان", null=True, blank=True)
    TIMEandDATE = models.DateTimeField(verbose_name="ساعت و روز کلاس", null=True)
    SerialOfClass = models.IntegerField(verbose_name="سریال کلاس", null=True)

    created_at = models.DateTimeField(default=timezone.now)

    Status_choises = ((1, 'معتبر'), (2, 'نامعتبر'))
    StatusofCredit = models.IntegerField(choices=Status_choises, verbose_name="وضعیت اعتبار کلاس", null=True)
    
    VariablePoetry = models.IntegerField(null=True, verbose_name="شهریه متغیر")

    def __str__(self):
        return str(self.Namelesson)



    

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
    