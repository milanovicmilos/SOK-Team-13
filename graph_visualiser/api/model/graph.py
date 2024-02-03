from typing import Optional

from api.exception.graph_exception import GraphException
from api.model.edge import Edge
from api.model.node import Node


class Graph:

    def __init__(self, nodes: list[Node] = None, edges: list[Edge] = None):
        self._nodes = nodes or []
        self._edges = edges or []

    @property
    def nodes(self) -> list[Node]:
        return self._nodes

    @property
    def edges(self) -> list[Edge]:
        return self._edges

    def add_node(self, node: Node):
        if node in self._nodes:
            raise GraphException("Node already exists")
        self._nodes.append(node)

    def add_edge(self, edge: Edge):
        if edge in self._edges:
            raise GraphException("Edge already exists")
        self._edges.append(edge)

    def remove_node(self, node: Node):
        if node not in self._nodes:
            raise GraphException("Node does not exist")
        self._edges = [edge for edge in self._edges if node not in (edge.source_node, edge.target_node)]
        self._nodes.remove(node)

    def remove_edge(self, edge: Edge):
        if edge not in self._edges:
            raise GraphException("Edge does not exist")
        self._edges.remove(edge)

    def find_node_by_id(self, node_id: int) -> Optional[Node]:
        for node in self._nodes:
            if node.node_id == node_id:
                return node
        return None

    def get_node_edges(self, node: Node) -> list[Edge]:
        return [edge for edge in self._edges if node in (edge.source_node, edge.target_node)]

    def get_node_source_edges(self, node: Node) -> list[Edge]:
        return [edge for edge in self._edges if edge.source_node == node]

    def get_node_target_edges(self, node: Node) -> list[Edge]:
        return [edge for edge in self._edges if edge.target_node == node]


