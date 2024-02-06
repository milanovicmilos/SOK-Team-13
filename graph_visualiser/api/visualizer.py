from abc import ABC, abstractmethod

from build.lib.graph_visualiser.api.model.graph import Graph


class Visualizer(ABC):
    def __init__(self, graph: Graph):
        """
        Constructor of the abstract class for graph visualization.
        """
        self.graph = graph
        pass

    @abstractmethod
    def generate_html(self):
        """
        Abstract method that generates an HTML representation of the graph.

        Returns:
        - str: HTML string representing the graph visualization.
        """
        pass

    @abstractmethod
    def set_graph(self, graph: Graph):
        """
        Abstract method that sets the graph to visualize.

        Parameters:
        - graph (Graph): Graph to visualize.
        """
        pass

    @abstractmethod
    def get_graph(self):
        """
        Abstract method that gets the graph to visualize.

        Returns:
        - Graph: Graph to visualize.
        """
        pass

    @abstractmethod
    def name(self):
        """
        Abstract method that gets the name of the visualizer.

        Returns:
        - str: Name of the visualizer.
        """
        pass

    @abstractmethod
    def identifier(self):
        """
        Abstract method that gets the identifier of the visualizer.

        Returns:
        - str: Identifier of the visualizer.
        """
        pass