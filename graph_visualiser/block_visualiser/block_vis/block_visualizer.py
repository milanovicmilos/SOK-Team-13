from jinja2 import FileSystemLoader, Environment
import os

from graph_visualiser.api.model.graph import Graph
from graph_visualiser.api.visualizer import Visualizer


class BlockVisualiser(Visualizer):
    def identifier(self):
        return "BlockVisualiser"

    def __init__(self):
        super().__init__(graph=None)

    def name(self):
        return "BlockVisualiser"

    def generate_html(self):
        context = {"graph": self.graph}

        env = Environment(loader=FileSystemLoader("C:/Users/Milos/PythonProjects/SOK-Team-13/D3Core/d3_primeri/templates"))
        print("VEPAR GEDZAAAAAAAAAAAAAAAAAAAAAa")

        for i in env.list_templates():
            print(i)
        template = env.get_template("block_visualizer_view.html")
        return template.render(context)

    def set_graph(self, graph: Graph):
        self.graph = graph

    def get_graph(self):
        return self.graph
