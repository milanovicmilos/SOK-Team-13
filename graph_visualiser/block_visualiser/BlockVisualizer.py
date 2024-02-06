from jinja2 import FileSystemLoader, Environment

from graph_visualiser.api.model.graph import Graph
from graph_visualiser.api.visualizer import Visualizer


class BlockVisualiser(Visualizer):
    def __init__(self, graph: Graph):
        super().__init__(graph)

    def name(self):
        return "BlockVisualiser"
    def generate_html(self):
        context = {"graph": self.graph}
        env = Environment(loader=FileSystemLoader("../block_visualiser"))
        template = env.get_template("BlockVisualiserView.html")
        return template.render(context)