from abc import ABC, abstractmethod

from graph_visualiser.api.model.graph import Graph


class DataSource(ABC):
    def __init__(self, url: str):
        """
        Constructor of the abstract class for data sources.

        Parameters:
        - url (str): URL of the data source.
        """
        self.url = url
        self.graph = Graph()
        self.data_getter = None

    @abstractmethod
    def configure(self):
        """
        Method for configuring the data source.
        """

        pass

    @abstractmethod
    def get_graph(self):
        """
        Method for getting the graph from the data source.

        Returns:
        - Graph: Data structure representing a graph.
        """
        pass

    @abstractmethod
    def create_node(self, html_content, link: str):
        """
        Method for creating a node in the graph.

        Parameters:
        - html_content (str): HTML content of the node.
        - link (str): URL of the node.

        Returns:
        - Node: Node created.
        """
        pass

    @abstractmethod
    def get_next_node(self, links, current_node, depth: int = 0):
        """
        Method for getting the next node in the graph.

        Parameters:
        - links (List[str]): URLs of the next nodes.
        - current_node (Node): Current node.
        - depth (int): Depth of the current node in the graph.
        """
        pass

    @abstractmethod
    def create_edge(self, node, current_node):
        """
        Method for creating an edge in the graph.

        Parameters:
        - node (Node): Node to connect.
        - current_node (Node): Current node.
        """
        pass

    @abstractmethod
    def identifier(self):
        pass

    @abstractmethod
    def naziv(self):
        pass
