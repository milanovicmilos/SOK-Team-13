from abc import ABC, abstractmethod


class Visualizer(ABC):
    def __init__(self, graph):
        """
        Constructor of the abstract class for graph visualization.

        Parameters:
        - graph (dict): The graph model used to generate the visualization.
        """
        self.graph = graph

    @abstractmethod
    def generate_html(self):
        """
        Abstract method that generates an HTML representation of the graph.

        Returns:
        - str: HTML string representing the graph visualization.
        """
        pass
