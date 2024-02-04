from abc import ABC, abstractmethod

from graph_visualiser.api.model.graph import Graph
from graph_visualiser.data_source_plugin.wiki_data_getter import WikiDataGetter


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
        self.recursion_depth = 0

    @abstractmethod
    def parse_data(self, data):
        """
        Method for parsing data and forming a graph.

        Parameters:
        - data: Data from the source, such as JSON, XML, CSV, etc.

        Returns:
        - Graph: Data structure representing a graph.
        """
        pass

    @abstractmethod
    def configure(self):
        """
        Method for configuring the data source.
        """

        pass

    @abstractmethod
    def get_required_parameters(self):
        """
        Method that returns a list of required input parameters for a specific data source.

        Returns:
        - List[str]: List of required input parameters.
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
