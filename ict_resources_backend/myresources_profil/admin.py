from data_seeder.admin import DataGeneratorAdmin
from django.contrib import admin
from .models import *


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    exclude = ('groups', 'is_active', 'is_staff', 'user_permissions', 'is_superuser')

    def save_related(self, request, form, formsets, change):
        super(CustomUserAdmin, self).save_related(request, form, formsets, change)

        obj = form.instance

        obj.set_password(obj.password)
        obj.save()

        # make changes to model instance
        profile = list(obj.profile.all().values_list())

        begin_url = CODE_STUDENT

        id_profile = profile[0][0]

        # on met les obj.is_admin, is_teacher,   a cause du frontend on veut la faciliter a trouver les admin, teacher
        if TEACHER == id_profile:
            begin_url = CODE_TEACHER
            to_add = Group.objects.get(name="TEACHER")  # get_or_create is a better option
            obj.groups.add(to_add)
            obj.is_teacher = True
            obj.save()

        if ADMIN == id_profile:
            begin_url = CODE_ADMIN
            to_add = Group.objects.get(name="ADMIN")  # get_or_create is a better option
            obj.groups.add(to_add)
            obj.is_staff = True
            obj.is_admin = True
            obj.save()

        if SUPERADMIN == id_profile:
            begin_url = CODE_SUPERADMIN
            to_add = Group.objects.get(name="SUPERADMIN")  # get_or_create is a better option
            obj.groups.add(to_add)
            obj.is_staff = True
            obj.save()

        if STUDENT == id_profile:
            begin_url = CODE_STUDENT
            to_add = Group.objects.get(name="STUDENT")  # get_or_create is a better option
            obj.groups.add(to_add)
            obj.is_staff = False
            obj.save()

        url = generate_url(obj.email, begin_url)
        send_activate_account_mail(obj.email, url)

    def __str__(self):
        return "josue"


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, DataGeneratorAdmin)
