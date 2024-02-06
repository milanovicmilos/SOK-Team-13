import pkg_resources
from django.apps import AppConfig


class D3PrimeriConfig(AppConfig):
    name = 'd3_primeri'
    plugini_ucitavanje = []

    def ready(self):
        self.plugini_ucitavanje = load_plugins("graph_visualiser.data_source")


def load_plugins(oznaka):
    url = "https://en.wikipedia.org/wiki/Formula_1"
    plugins = []

    list_of_entry_points = list(pkg_resources.iter_entry_points(group=oznaka))
    # print(list_of_entry_points)

    for ep in pkg_resources.iter_entry_points(group=oznaka):
        o = ep.load()
        parser = o(url)
        plugins.append(parser)
    return plugins
