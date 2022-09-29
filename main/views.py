from django.shortcuts import render,redirect
from .models import Demande

def demande(request):
    if request.method=="POST":
        print(request.POST)
        demende = Demande.objects.create(nom = request.POST["nom"],prenom = request.POST["prenom"],mail = request.POST["mail"],wtsp = request.POST["wtsp"],niveau = request.POST["niveau"],filiere = request.POST["filiere"],for_av_eta = request.POST["for_av_eta"],for_av_fil = request.POST["for_av_fil"],interet_domaine = request.POST["interet_domaine"],interet_prolang = request.POST["interet_prolang"],parti_comp_info = request.POST["parti_comp_info"],parti_comp_math = request.POST["parti_comp_math"],motivation = request.POST["motivation"],message = request.POST["message"])

        return redirect("merci")
    content={}
    return render(request,"index.html",content)


def merci(request):
    return render(request,"merci.html",{})
