from django.apps.registry import apps
from django.shortcuts import render, redirect



def index(request):
    print("KRMADIJA")
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    visualizer_plugins = apps.get_app_config('d3_primeri').plugini_visualizer_ucitavanje
    print(plugini)
    print(visualizer_plugins)
    return render(request, "index.html", {"title": "Index", "plugini_ucitavanje": plugini, "plugini_visualizer_ucitavanje": visualizer_plugins})


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
            i.set_url(apps.get_app_config('d3_primeri').url)
            apps.get_app_config('d3_primeri').graph = i.get_graph()
            print("wdwdwwd")
    return redirect('index')


def ucitavanje_plugin_visualizer(request, id):
    request.session['izabran_plugin_visualizer_ucitavanje'] = id
    plugini = apps.get_app_config('d3_primeri').plugini_visualizer_ucitavanje
    print(plugini)
    for i in plugini:
        print("BRMEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        print(i.identifier())
        print(id)
        if i.identifier() == id:
            print("vepar")
            i.set_graph(apps.get_app_config('d3_primeri').graph)
            print("wdwdwwd")
            return render(request, 'index.html', {'block_visualizer_view': i.generate_html(),
                                                  "plugini_ucitavanje": apps.get_app_config('d3_primeri').plugini_ucitavanje,
                                                  "plugini_visualizer_ucitavanje": apps.get_app_config('d3_primeri').plugini_visualizer_ucitavanje
                                                  })

    return redirect('index')


def your_view_function(request):
    if request.method == 'GET':
        # Get the value from the input field with the name "url_pretraga"
        url_pretraga_value = request.GET.get('url_pretraga', None)

        # Now you can use the 'url_pretraga_value' as needed
        if url_pretraga_value:
            # Do something with the value, for example, print it
            apps.get_app_config('d3_primeri').url = url_pretraga_value
            print("Inputted URL:", url_pretraga_value)
            print(apps.get_app_config('d3_primeri').url)

    # Your other view logic goes here

    return render(request, 'index.html', {
                                                  "plugini_ucitavanje": apps.get_app_config('d3_primeri').plugini_ucitavanje,
                                                  "plugini_visualizer_ucitavanje": apps.get_app_config('d3_primeri').plugini_visualizer_ucitavanje
                                                  })
