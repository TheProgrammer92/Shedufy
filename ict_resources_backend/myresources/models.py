from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from rest_framework.authtoken.models import Token


# Create your models here.

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return self.user.password


class Adresse(models.Model):
    code_postal = models.CharField(max_length=10, primary_key=True)
    email = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)


class Emploi_de_temps(models.Model):
    code_Et = models.CharField(max_length=10, primary_key=True, blank=False)
    date_debut = models.DateTimeField(default=timezone.now)
    date_fin = models.DateTimeField(default=timezone.now)


class Classe(models.Model):
    code_classe = models.CharField(max_length=10, primary_key=True)
    emploi_de_temps = models.OneToOneField(Emploi_de_temps, on_delete=models.CASCADE)


class Etudiants(models.Model):
    matricule_et = models.CharField(max_length=10, primary_key=True, blank=False)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateTimeField(default=timezone.now)
    adresse = models.OneToOneField(Adresse, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)


class Enseignant(models.Model):
    matricule_ens = models.CharField(max_length=10, primary_key=True, blank=False)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateTimeField(default=timezone.now)
    adresse = models.OneToOneField(Adresse, on_delete=models.CASCADE)
    emploi_de_temps = models.OneToOneField(Emploi_de_temps, on_delete=models.CASCADE)


class Admin(models.Model):
    matricule_admin = models.CharField(max_length=10, primary_key=True, blank=False)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateTimeField(default=timezone.now)
    adresse = models.OneToOneField(Adresse, on_delete=models.CASCADE)


class Categorie(models.Model):
    code_categorie = models.CharField(max_length=10, primary_key=True)
    nom_categorie = models.CharField(max_length=50)


class Materiel(models.Model):
    code_materiel = models.CharField(max_length=10, primary_key=True)
    nom = models.CharField(max_length=50)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)


class Emprunt(models.Model):
    numero = models.IntegerField(primary_key=True, blank=False)
    date_emprunt = models.DateTimeField(default=timezone.now)
    date_remise = models.DateTimeField(default=timezone.now)
    enseignant = models.ManyToManyField(Enseignant)
    materiel = models.ManyToManyField(Materiel)


class Salle(models.Model):
    id_salle = models.CharField(max_length=10, primary_key=True)
    emploi_de_temps = models.OneToOneField(Emploi_de_temps, on_delete=models.CASCADE)
    classe = models.ManyToManyField(Classe)


class Cours(models.Model):
    code_cours = models.CharField(max_length=10, primary_key=True)
    intitulé = models.CharField(max_length=50)
    etudiant = models.ManyToManyField(Etudiants)
    enseignant = models.ManyToManyField(Enseignant)
    date_debut = models.DateTimeField(default=timezone.now)
    date_fin = models.DateTimeField(default=timezone.now)
    emploi_de_temps = models.OneToOneField(Emploi_de_temps, on_delete=models.CASCADE)


class Suivre(models.Model):
    matricule_et = models.ForeignKey(Etudiants, on_delete=models.CASCADE)
    code_cours = models.ForeignKey(Cours, on_delete=models.CASCADE)


class Faire_emprunt(models.Model):
    matricule_ens = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    numero = models.ForeignKey(Emprunt, on_delete=models.CASCADE)


class Dispenser(models.Model):
    matricule_ens = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    code_cours = models.ForeignKey(Cours, on_delete=models.CASCADE)


class Concerner(models.Model):
    code_materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    numero = models.ForeignKey(Emprunt, on_delete=models.CASCADE)


class Abriter(models.Model):
    id_salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    code_classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
