import uuid

from graph_visualiser.api.data_source import DataSource
from graph_visualiser.api.model.edge import Edge
from graph_visualiser.api.model.graph import Graph
from graph_visualiser.api.model.node import Node
from graph_visualiser.data_source_plugin.wiki_data_getter import WikiDataGetter


class DataSourceHTML(DataSource):
    def __init__(self, url: str):
        super().__init__(url)

    def parse_data(self, data):
        """
        Method for parsing HTML data and forming a graph.

        Parameters:
        - data: HTML data from the source.

        Returns:
        - Graph: Data structure representing a graph.
        """
        # Implement the logic for parsing HTML data here
        pass

    def configure(self):
        """
        Method for configuring the HTML data source.
        """
        wiki_data_getter = WikiDataGetter(self.url)
        self.data_getter = wiki_data_getter

        return self.data_getter.get_node_html_data()

    def get_required_parameters(self):
        """
        Method that returns a list of required input parameters for the HTML data source.

        Returns:
        - List[str]: List of required input parameters.
        """
        # Implement the logic for getting the required parameters here
        pass

    def get_graph(self) -> Graph:
        """
        Method for getting the graph from the HTML data source.

        Returns:
        - Graph: Data structure representing a graph.
        """
        html_content, links = self.configure()
        current_node = self.create_node(html_content, self.url)
        self.get_next_node(links, current_node)
        return self.graph

    def create_node(self, html_content, link: str) -> Node:
        node = Node(link, html_content)
        self.graph.add_node(node)
        return node

    def get_next_node(self, links, current_node):
        if self.graph.get_graph_size() > 20:
            return
        if self.recursion_depth > 3:
            self.recursion_depth = 0
            return
        self.recursion_depth += 1
        for link in links:
            self.data_getter.set_url(link)
            html_content, new_links = self.data_getter.get_node_html_data()
            node = self.create_node(html_content, link)
            self.create_edge(node, current_node)
            self.get_next_node(new_links, node)
        return

    def create_edge(self, node: Node, current_node: Node):
        edge = Edge(current_node, node)
        self.graph.add_edge(edge)
