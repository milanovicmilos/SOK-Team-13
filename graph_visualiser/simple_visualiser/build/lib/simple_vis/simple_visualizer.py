from jinja2 import FileSystemLoader, Environment
import os

from graph_visualiser.api.model.graph import Graph
from graph_visualiser.api.visualizer import Visualizer

class SimpleVisualiser(Visualizer):
    def identifier(self):
        return "SimpleVisualiser"

    def __init__(self):
        super().__init__(graph=None)

    def name(self):
        return "SimpleVisualiser"

    def generate_html(self):
        context = {"graph": self.graph}

        env = Environment(loader=FileSystemLoader("../graph_visualiser/simple_visualiser/simple_vis"))

        for i in env.list_templates():
            print(i)
        template = env.get_template("simple_visualizer_view.html")
        return template.render(context)

    def set_graph(self, graph: Graph):
        self.graph = graph

    def get_graph(self):
        return self.graph
