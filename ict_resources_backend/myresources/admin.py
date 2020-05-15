from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(Categorie)
admin.site.register(Enseignant)
admin.site.register(Classe)
admin.site.register(Adresse)
admin.site.register(Emploi_de_temps)
admin.site.register(Admin)
admin.site.register(Materiel)
admin.site.register(Emprunt)
admin.site.register(Salle)
admin.site.register(Cours)
admin.site.register(Suivre)
admin.site.register(Faire_emprunt)
admin.site.register(Dispenser)
admin.site.register(Concerner)
admin.site.register(Abriter)



