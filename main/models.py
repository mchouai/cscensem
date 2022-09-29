from django.db import models

class Demande(models.Model):
    date_demande = models.DateField(auto_now=True)
    nom = models.CharField(max_length=30)
    mail = models.CharField(max_length=30,default=None)
    wtsp = models.CharField(max_length=30,default=None)
    prenom = models.CharField(max_length=30)
    niveau = models.CharField(max_length=30)
    filiere = models.CharField(max_length=30)
    for_av_eta = models.CharField(max_length=30)
    for_av_fil = models.CharField(max_length=30)
    interet_domaine =  models.CharField(max_length=30)
    interet_prolang = models.CharField(max_length=30)
    parti_comp_info = models.BooleanField(default=None,null=True)
    parti_comp_math = models.BooleanField(default=None,null=True)
    motivation = models.CharField(max_length=500)
    message = models.CharField(max_length=500)
