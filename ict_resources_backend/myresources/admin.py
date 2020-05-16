from django.contrib import admin

# Register your models here.


from myresources.models import *

admin.site.register(Category)
admin.site.register(userProfile)
admin.site.register(Teacher)
admin.site.register(Classe)
admin.site.register(Adress)
admin.site.register(Students)
admin.site.register(Schedule)

admin.site.register(Equipment)
admin.site.register(Borrow)
admin.site.register(Room)
admin.site.register(Course)
admin.site.register(Follow)
admin.site.register(Borrowing)
admin.site.register(Dispense)
admin.site.register(Concern)
admin.site.register(Shelter)



