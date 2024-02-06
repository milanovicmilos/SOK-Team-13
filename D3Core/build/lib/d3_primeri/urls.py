from django.urls import path

from d3_primeri import prodavnica_view

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ucitavanje/plugin/<str:id>', views.ucitavanje_plugin, name="ucitavanje_plugin"),

    path('primer/prodavnica/force/layout', prodavnica_view.foce_layout, name="prodavnica_force_layout"),
    path('primer/prodavnica/tree/layout', prodavnica_view.tree_layout, name="prodavnica_tree_layout"),

    path('primer/pan/zoom', views.primerPanZoom, name="primerPanZoom"),
]
