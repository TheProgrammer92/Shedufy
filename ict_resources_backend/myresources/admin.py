from django.contrib import admin

# Register your models here.


from myresources.models import *

from myresources_profil.models import *

admin.site.register(CustomUser)
admin.site.register(Teacher)
admin.site.register(CategoryClasse)
admin.site.register(CategoryCourse)
admin.site.register(Classe)
admin.site.register(Adress)
admin.site.register(Students)
admin.site.register(Schedule)
admin.site.register(ReservationSchedule)

admin.site.register(Equipment)
admin.site.register(Borrow)

admin.site.register(Course)
admin.site.register(Follow)
admin.site.register(Borrowing)
admin.site.register(Dispense)
admin.site.register(Concern)
