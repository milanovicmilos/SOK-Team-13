from graph_visualiser.api.data_source import DataSource
from graph_visualiser.api.model.edge import Edge
from graph_visualiser.api.model.graph import Graph
from graph_visualiser.api.model.node import Node
from graph_visualiser.data_source_plugin.wiki_data_getter import WikiDataGetter


class DataSourceHTML(DataSource):
    def __init__(self, url: str):
        super().__init__(url)

    def configure(self):
        """
        Method for configuring the HTML data source.
        """
        wiki_data_getter = WikiDataGetter(self.url)
        self.data_getter = wiki_data_getter

        return self.data_getter.get_node_html_data()

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
        """
        Method for creating a node in the graph.
        :param html_content:
        :param link:
        :return:
        """
        node = Node(link, html_content)
        self.graph.add_node(node)
        return node

    def get_next_node(self, links, current_node, depth: int = 0) -> None:
        """
        Method for getting the next node in the graph.
        :param links:
        :param current_node:
        :param depth:
        :return:
        """
        if self.graph.get_graph_size() > 5:
            return
        if depth > 3:
            return
        for link in links:
            self.data_getter.set_url(link)
            html_content, new_links = self.data_getter.get_node_html_data()
            node = self.create_node(html_content, link)
            self.create_edge(node, current_node)
            self.get_next_node(new_links, node, depth + 1)
        return

    def create_edge(self, node: Node, current_node: Node) -> None:
        """
        Method for creating an edge in the graph.
        :param node:
        :param current_node:
        :return:
        """
        edge = Edge(current_node, node)
        self.graph.add_edge(edge)

    def identifier(self):
        return "HTML"

    def naziv(self):
        return "HTML"


    def set_url(self, url: str):
        self.url = url

