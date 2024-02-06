from django.apps.registry import apps
from django.shortcuts import render, redirect

from d3_primeri.models import Prodavnica, Artikal


def index(request):
    print("KRMADIJA")
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    print(plugini)
    return render(request, "index.html", {"title": "Index", "plugini_ucitavanje": plugini})


def ucitavanje_plugin(request, id):
    request.session['izabran_plugin_ucitavanje'] = id
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    print(plugini)
    for i in plugini:
        print("KRMEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        print(i.identifier())
        print(id)
        if i.identifier() == id:
            print("vepar")
            i.get_graph()
            print("wdwdwwd")
    return redirect('index')


def primer1(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request, "primer1.html", {"title": "Primer1", "plugini_ucitavanje": plugini})


def primer2(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request, "primer2.html", {"title": "Primer2", "plugini_ucitavanje": plugini})


def primer3(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request, "primer3.html", {"title": "Primer3", "plugini_ucitavanje": plugini})


def primer4(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request, "primer4.html", {"title": "Primer4", "plugini_ucitavanje": plugini})


def primer5(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request, "primer5.html", {"title": "Primer5", "plugini_ucitavanje": plugini})


def primer6(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    prodavnice = Prodavnica.objects.all()
    artikli = Artikal.objects.all()
    return render(request, "primer6.html",
                  {"title": "Primer prodavnica force layout",
                   "plugini_ucitavanje": plugini,
                   "prodavnice": prodavnice,
                   "artikli": artikli})


def primerPanZoom(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request, "primerPanZoom.html", {"title": "Primer Pan Zoom", "plugini_ucitavanje": plugini})
