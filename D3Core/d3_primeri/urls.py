from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ucitavanje/plugin/<str:id>', views.ucitavanje_plugin, name="ucitavanje_plugin"),

    path('ucitavanje/plugin/visualizer/<str:id>', views.ucitavanje_plugin_visualizer, name="ucitavanje_plugin_visualizer"),

    path('yourview/function', views.your_view_function, name="your_view_function"),

    path('search/function', views.search, name="search_function"),
]
