from django.apps.registry import apps
from django.shortcuts import render, redirect

from d3_primeri.models import Prodavnica, Artikal


def index(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request,"index.html",{"title":"Index","plugini_ucitavanje":plugini})

def ucitavanje_plugin(request,id):
    request.session['izabran_plugin_ucitavanje']=id
    plugini=apps.get_app_config('d3_primeri').plugini_ucitavanje
    for i in plugini:
        if i.identifier() == id:
            i.get_graph()
    return redirect('index')

def primer1(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request,"primer1.html",{"title":"Primer1","plugini_ucitavanje":plugini})


def primer2(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request, "primer2.html", {"title": "Primer2","plugini_ucitavanje":plugini})


def primer3(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request, "primer3.html", {"title": "Primer3","plugini_ucitavanje":plugini})

def primer4(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request, "primer4.html", {"title": "Primer4","plugini_ucitavanje":plugini})

def primer5(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request, "primer5.html", {"title": "Primer5","plugini_ucitavanje":plugini})

def primer6(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    prodavnice=Prodavnica.objects.all()
    artikli=Artikal.objects.all()
    return render(request,"primer6.html",
                  {"title":"Primer prodavnica force layout",
                   "plugini_ucitavanje": plugini,
                   "prodavnice":prodavnice,
                   "artikli":artikli})


def primerPanZoom(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request, "primerPanZoom.html", {"title": "Primer Pan Zoom","plugini_ucitavanje":plugini})