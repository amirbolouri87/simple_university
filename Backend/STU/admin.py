from django.contrib import admin

# Register your models here.



from .models import Collage , Major , Lesson , ChoiseLesson , Authticat , Register , Teacher




admin.site.register(Collage)
admin.site.register(Major)
admin.site.register(Lesson)
admin.site.register(ChoiseLesson)
admin.site.register(Authticat)
admin.site.register(Register)
admin.site.register(Teacher)