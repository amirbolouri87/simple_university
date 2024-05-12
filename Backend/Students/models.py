from django.db import models
from django.utils import timezone
# Create your models here.
from .rabbitmq_sender import RabbitMQSender


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


class Teacher(models.Model):
    class Meta:
        verbose_name = "اساتید"
        verbose_name_plural = "اساتید"



    Fullname =models.CharField(max_length=30 , verbose_name="نام استاد")
    NationalNumber = models.IntegerField(verbose_name="کدملی")
    Major=models.ForeignKey(Major , on_delete=models.CASCADE , verbose_name="رشته")

    Grade_choices = ((0, 'فوق لیسانس') , (1 , 'دکتری'))
    GradeofCredit = models.CharField(choices=Grade_choices , verbose_name="مدرک" , null=True)

    def __str__(self) :
        return self.Fullname
    

class ChoiseUnit(models.Model):
    class Meta:
        verbose_name = "انتخاب واحد"
        verbose_name_plural = "انتخاب واحد"

    id = models.AutoField(primary_key=True)
    Namelesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True , verbose_name="نام درس")
    ClassDayTime = models.DateTimeField(verbose_name="زمان و تاریخ شروع کلاس", null=True) 
    ExamDateTime = models.DateTimeField(verbose_name="  زمان و تاریخ امتحان", null=True, blank=True)
    TIMEandDATE = models.DateTimeField(verbose_name="ساعت و روز کلاس", null=True)
    SerialOfClass = models.IntegerField(verbose_name="سریال کلاس", null=True)
    EnterYears = models.IntegerField(null =True , verbose_name="سال ورودی" , )
    NameofTeacher = models.ForeignKey(Teacher , on_delete=models.CASCADE , verbose_name="نام استاد" , null = True)

    Status_choices = ((1, 'معتبر'), (2, 'نامعتبر'))
    StatusofCredit = models.IntegerField(choices=Status_choices, verbose_name="وضعیت اعتبار کلاس", null=True)

        
    VariablePoetry = models.IntegerField(null=True, verbose_name="شهریه متغیر")
    Capacity = models.IntegerField(null =True , verbose_name="ظرفیت کلاس")

    @property

    def is_entery_year_valid(self):
        current_year = timezone.now().year

        if self.EnterYears:
            return self.EnterYears >= (current_year - 4)
        return False
    

    @property
    def is_entery_capacity(self):
        
        if self.Capacity >= 20 :
            return self.Capacity 
        return False

    def __str__(self):
        return str(self.Namelesson)



    

sender = RabbitMQSender()

sample_message = {
   # lesson_name = choise_unit.Namelesson.NameOfLesson if choise_unit.Namelesson else None
    #"ClassDayTime" : ChoiseUnit.ClassDayTime.isoformat() if ChoiseUnit.ClassDayTime else None,
    #"ExamDateTime": ChoiseUnit.ExamDateTime.isoformat() if ChoiseUnit.ExamDateTime else None,
   # "TIMEandDATE" : ChoiseUnit.TIMEandDATE.isoformat() if ChoiseUnit.TIMEandDATE else None ,
   # "SerialOfClass":
   # "EnterYears":
    #"NameofTeacher" :
    #"StatusofCredit":
    #"VariablePoetry" :
    #"Capacity" :
}
sender.send_to_queue(sample_message)

sender.close_connection()