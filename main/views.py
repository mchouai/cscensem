from django.shortcuts import render,redirect
from .models import Demande
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

def loginpage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("main")
        else:
            messages.info(request,"Nom d'utilisateur ou mot de passe incorrecte")
    return render(request,"login.html",{})

def demande(request):
    if request.method=="POST":
        print(request.POST)
        demende = Demande.objects.create(nom = request.POST["nom"],prenom = request.POST["prenom"],mail = request.POST["mail"],wtsp = request.POST["wtsp"],niveau = request.POST["niveau"],filiere = request.POST["filiere"],for_av_eta = request.POST["for_av_eta"],for_av_fil = request.POST["for_av_fil"],interet_domaine = request.POST["interet_domaine"],interet_prolang = request.POST["interet_prolang"],parti_comp_info = request.POST["parti_comp_info"],parti_comp_math = request.POST["parti_comp_math"],motivation = request.POST["motivation"],message = request.POST["message"])
        return redirect("merci")
    content={}
    return render(request,"index.html",content)


def merci(request):
    return render(request,"merci.html",{})

@login_required(login_url="loginpage")
def admin(request):
    demandes=Demande.objects.all()
    content={"demandes":demandes,"n":len(demandes)}
    return render(request,"admin.html",content)


@login_required(login_url="loginpage")
def demandes(request,id):
    demandes=list(Demande.objects.all())
    demande=Demande.objects.get(pk=id)
    precedent=demandes[demandes.index(demande)-1]
    suivant=demandes[(demandes.index(demande)+1)%len(demandes)]
    content={"demande":demande,"precedent":precedent,"suivant":suivant}
    return render(request,"demande.html",content)
