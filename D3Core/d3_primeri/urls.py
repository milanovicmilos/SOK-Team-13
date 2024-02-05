from django.urls import path

from d3_primeri import prodavnica_view

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ucitavanje/plugin/<str:id>', views.ucitavanje_plugin, name="ucitavanje_plugin"),
    path('primer1', views.primer1, name="primer1"),
    path('primer2', views.primer2, name="primer2"),
    path('primer3', views.primer3, name="primer3"),

    path('primer4', views.primer4, name="primer4"),

    path('primer5', views.primer5, name="primer5"),
    path('primer6', views.primer6, name="primer6"),

    path('primer/prodavnica/force/layout', prodavnica_view.foce_layout, name="prodavnica_force_layout"),
    path('primer/prodavnica/tree/layout', prodavnica_view.tree_layout, name="prodavnica_tree_layout"),

    path('primer/pan/zoom', views.primerPanZoom, name="primerPanZoom"),
]
