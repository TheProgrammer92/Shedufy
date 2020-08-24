from django.contrib import admin

# Register your models here.


from myresources.models import *
from functions.functions import *
from myresources_profil.models import *
from data_seeder.admin import DataGeneratorAdmin


admin.site.register(CategoryClasse, DataGeneratorAdmin)
admin.site.register(CategoryCourse, DataGeneratorAdmin)
admin.site.register(Classe, DataGeneratorAdmin)
admin.site.register(Schedule, DataGeneratorAdmin)
admin.site.register(Etat, DataGeneratorAdmin)
admin.site.register(TypeSchedule, DataGeneratorAdmin)
admin.site.register(ReservationSchedule, DataGeneratorAdmin)
admin.site.register(Department, DataGeneratorAdmin)
admin.site.register(Notifications, DataGeneratorAdmin)
admin.site.register(CategorieNotifications, DataGeneratorAdmin)
admin.site.register(FiliereCategorie, DataGeneratorAdmin)
admin.site.register(Filiere, DataGeneratorAdmin)
admin.site.register(Level, DataGeneratorAdmin)

admin.site.register(Equipment, DataGeneratorAdmin)
admin.site.register(Borrow, DataGeneratorAdmin)

admin.site.register(Course, DataGeneratorAdmin)


class CustomUserAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):

        super().save_model(self, request, obj, form, change)

        url = generate_url(request.GET['email'])
        send_activate_account_mail(request.GET['email'], url)




