from django.contrib import admin

# Register your models here.


from myresources.models import *



admin.site.register(UserProfile)
admin.site.register(Teacher)
admin.site.register(Classe)
admin.site.register(Adress)
admin.site.register(Students)
admin.site.register(Schedule)

admin.site.register(Equipment)
admin.site.register(Borrow)

admin.site.register(Course)
admin.site.register(Follow)
admin.site.register(Borrowing)
admin.site.register(Dispense)
admin.site.register(Concern)




