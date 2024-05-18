from django.contrib import admin

# Register your models here.



from .models import Collage , Major ,Authticat , Register  , Borrow , Liberary




admin.site.register(Collage)
admin.site.register(Major)
admin.site.register(Authticat)
admin.site.register(Register)
admin.site.register(Borrow)
admin.site.register(Liberary)