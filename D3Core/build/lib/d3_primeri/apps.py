import pkg_resources
from django.apps import AppConfig


class D3PrimeriConfig(AppConfig):
    name = 'd3_primeri'
    plugini_ucitavanje = []
    plugini_visualizer_ucitavanje = []
    graph = None
    url = "https://en.wikipedia.org/wiki/Formula_1"

    def ready(self):
        self.plugini_ucitavanje = load_plugins("graph_visualiser.data_source")
        self.plugini_visualizer_ucitavanje = load_visualizer_plugins("graph_visualiser.visualizer")


def load_visualizer_plugins(oznaka):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=oznaka):
        o = ep.load()
        parser = o()
        plugins.append(parser)
    print("LOAD VISUALIZER PLUGINS: ", plugins)
    return plugins


def load_plugins(oznaka):

    plugins = []

    list_of_entry_points = list(pkg_resources.iter_entry_points(group=oznaka))
    # print(list_of_entry_points)

    for ep in pkg_resources.iter_entry_points(group=oznaka):
        o = ep.load()
        print("prasence")
        print(D3PrimeriConfig.url)
        parser = o(D3PrimeriConfig.url)
        plugins.append(parser)
    return plugins


def set_a_graph(graph):
    D3PrimeriConfig.graph = graph
    print("SET GRAPH")
    print(D3PrimeriConfig.graph)


def get_a_graph():
    return D3PrimeriConfig.graph
