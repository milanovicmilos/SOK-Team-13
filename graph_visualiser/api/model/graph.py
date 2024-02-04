from typing import Optional, List

from graph_visualiser.api.model.edge import Edge
from graph_visualiser.api.model.node import Node


class Graph:
    """
    This class represents a graph data structure. It contains methods for adding and removing nodes and edges,
    finding a node by its id, and getting the edges associated with a node.
    """

    def __init__(self, nodes: List[Node] = None, edges: List[Edge] = None):
        self._nodes = nodes or []
        self._edges = edges or []

    @property
    def nodes(self) -> List[Node]:
        return self._nodes

    @property
    def edges(self) -> List[Edge]:
        return self._edges

    def add_node(self, node: Node):
        if any(existing_node.node_id == node.node_id for existing_node in self._nodes):
            # raise GraphException("Node already exists")
            return
        self._nodes.append(node)

    def add_edge(self, edge: Edge):
        if any(
                existing_edge.source_node.node_id == edge.source_node.node_id and existing_edge.target_node.node_id == edge.target_node.node_id
                for existing_edge in self._edges):
            # raise GraphException("Edge already exists")
            return
        self._edges.append(edge)

    def remove_node(self, node: Node):
        if node not in self._nodes:
            # raise GraphException("Node does not exist")
            return
        self._edges = [edge for edge in self._edges if node not in (edge.source_node, edge.target_node)]
        self._nodes.remove(node)

    def remove_edge(self, edge: Edge):
        if edge not in self._edges:
            # raise GraphException("Edge does not exist")
            return
        self._edges.remove(edge)

    def find_node_by_id(self, node_id: int) -> Optional[Node]:
        for node in self._nodes:
            if node.node_id == node_id:
                return node
        return None

    def get_node_edges(self, node: Node) -> List[Edge]:
        return [edge for edge in self._edges if node in (edge.source_node, edge.target_node)]

    def get_node_source_edges(self, node: Node) -> List[Edge]:
        return [edge for edge in self._edges if edge.source_node == node]

    def get_node_target_edges(self, node: Node) -> List[Edge]:
        return [edge for edge in self._edges if edge.target_node == node]

    def get_graph_size(self) -> int:
        return len(self._nodes)
