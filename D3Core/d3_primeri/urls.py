from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ucitavanje/plugin/<str:id>', views.ucitavanje_plugin, name="ucitavanje_plugin"),

    path('ucitavanje/plugin/visualizer/<str:id>', views.ucitavanje_plugin_visualizer, name="ucitavanje_plugin_visualizer"),
]
