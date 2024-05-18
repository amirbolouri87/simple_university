# Generated by Django 5.0.4 on 2024-05-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STU', '0006_register_admission_register_dataenrollment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='password_register',
        ),
        migrations.AlterField(
            model_name='choiselesson',
            name='ClassDayTime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='زمان و تاریخ شروع کلاس'),
        ),
        migrations.AlterField(
            model_name='choiselesson',
            name='ExamDateTime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='  زمان و تاریخ امتحان'),
        ),
        migrations.AlterField(
            model_name='register',
            name='TermEnteryCode',
            field=models.IntegerField(null=True, verbose_name='کد ترم ورودی'),
        ),
    ]
