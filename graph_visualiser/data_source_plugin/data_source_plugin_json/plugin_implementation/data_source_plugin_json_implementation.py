from graph_visualiser.api.data_source import DataSource
from graph_visualiser.api.model.edge import Edge
from graph_visualiser.api.model.graph import Graph
from graph_visualiser.api.model.node import Node
from graph_visualiser.data_source_plugin.wiki_data_getter import WikiDataGetter


class DataSourceJSON(DataSource):

    def __init__(self, url: str):
        super().__init__(url)

    def configure(self):
        wiki_data_getter = WikiDataGetter(self.url)
        self.data_getter = wiki_data_getter
        return self.data_getter.get_node_json_data()

    def get_graph(self) -> Graph:
        json_data = self.configure()
        current_node = self.create_node(json_data["data"], self.url)
        self.get_next_node(json_data["links"], current_node)
        return self.graph

    def create_node(self, html_content, link: str) -> Node:
        node = Node(link, html_content)
        self.graph.add_node(node)
        return node

    def get_next_node(self, links, current_node, depth: int = 0) -> None:
        if self.graph.get_graph_size() > 60:
            return
        if depth > 3:
            return
        for link in links:
            self.data_getter.set_url(link)
            json_data = self.data_getter.get_node_json_data()
            node = self.create_node(json_data["data"], link)
            self.create_edge(node, current_node)
            self.get_next_node(json_data["links"], node, depth + 1)
        return

    def create_edge(self, node: Node, current_node: Node) -> None:
        edge = Edge(current_node, node)
        self.graph.add_edge(edge)
