from django.apps.registry import apps
from django.shortcuts import render, redirect
import os
from jinja2 import Environment, FileSystemLoader


def index(request):
    print("KRMADIJA")
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    visualizer_plugins = apps.get_app_config('d3_primeri').plugini_visualizer_ucitavanje
    print(plugini)
    print(visualizer_plugins)
    return render(request, "index.html", {"title": "Index", "plugini_ucitavanje": plugini,
                                          "plugini_visualizer_ucitavanje": visualizer_plugins})


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
            apps.get_app_config('d3_primeri').graph = i.get_graph()
            print("wdwdwwd")
    return redirect('index')


def ucitavanje_plugin_visualizer(request, id):
    request.session['izabran_plugin_visualizer_ucitavanje'] = id
    plugini = apps.get_app_config('d3_primeri').plugini_visualizer_ucitavanje
    print(plugini)
    for i in plugini:
        print(i.identifier())
        print(id)
        if i.identifier() == id:
            i.set_graph(apps.get_app_config('d3_primeri').graph)
            context = {"graph": apps.get_app_config('d3_primeri').graph}
            current_script_path = os.path.realpath(__file__)
            script_directory = os.path.dirname(current_script_path)
            folder_path = os.path.join(script_directory, './templates')
            print("Folder Path:", folder_path)
            env = Environment(loader=FileSystemLoader(folder_path))
            bird_template = env.get_template("bird_view.html")
            tree_template = env.get_template("tree_view.html")

            return render(request, 'index.html', {
                'bird_view': bird_template.render(context),
                'tree_view': tree_template.render(context),
                'block_visualizer_view': i.generate_html(),
                "plugini_ucitavanje": apps.get_app_config(
                    'd3_primeri').plugini_ucitavanje,
                "plugini_visualizer_ucitavanje": apps.get_app_config(
                    'd3_primeri').plugini_visualizer_ucitavanje,
                "bird_view_rendered": True,
            })

    return redirect('index')

