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

def primerPanZoom(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request, "primerPanZoom.html", {"title": "Primer Pan Zoom", "plugini_ucitavanje": plugini})
