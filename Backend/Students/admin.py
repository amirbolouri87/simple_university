from django.contrib import admin
from .models import Major , Lesson , ChoiseUnit , Teacher

# Register your models here.
admin.site.register(Lesson)
admin.site.register(ChoiseUnit)
admin.site.register(Teacher)
admin.site.register(Major)
