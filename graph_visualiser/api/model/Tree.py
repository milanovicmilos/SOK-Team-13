from typing import List, Optional
from graph_visualiser.api.model.Node import Node
from graph_visualiser.api.model.Edge import Edge


class TreeNode:
    """
    A node in a tree.
    """

    def __init__(self, value: Node, children: Optional[List['TreeNode']] = None):
        """
        Initializes a new instance of TreeNode.

        Parameters:
        - value: The value of the node.
        - children: The children of the node.
        """
        self.value = value
        self.children = children if children is not None else []

    def add_child(self, child: 'TreeNode'):
        """
        Adds a child to the node.

        Parameters:
        - child: The child to add.
        """
        self.children.append(child)

    def remove_child(self, child: 'TreeNode'):
        """
        Removes a child from the node.

        Parameters:
        - child: The child to remove.
        """
        self.children.remove(child)

    def __str__(self):
        return f"TreeNode({self.value}, {self.children})"


class Tree:
    """
    A tree.
    """

    def __init__(self, root: Node, directed: bool):
        """
        Initializes a new instance of Tree.

        Parameters:
        - root: The root of the tree.
        - directed: Whether the tree is directed or not.
        """
        self.root = TreeNode(root)
        self.directed = directed

    def add_node(self, parent: Node, child: Node):
        """
        Adds a node to the tree.

        Parameters:
        - parent: The parent of the node.
        - child: The child to add.
        """
        parent_node = self.find_node(self.root, parent)
        if parent_node is not None:
            parent_node.add_child(TreeNode(child))

    def remove_node(self, node: Node):
        """
        Removes a node from the tree.

        Parameters:
        - node: The node to remove.
        """
        parent = self.find_parent(self.root, node)
        if parent is not None:
            parent.remove_child(node)

    def update_tree(self, target_node: Node, graph_edges: List[Edge]) -> None:
        """
        Updates the tree with the given target node and graph edges.

        Parameters:
        - target_node: The target node to update the tree with.
        - graph_edges: The edges of the graph.
        """
        self.root = self.update_tree_recursive(self.root, target_node, graph_edges)

    def create_tree(self, current_node: Node, graph_edges: List[Edge], visited_nodes: set) -> Optional[TreeNode]:
        """Recursively build the tree starting from the current node.

        Parameters:
        - current_node: The current node.
        - graph_edges: The edges of the graph.
        - visited_nodes: The set of visited nodes.

        Returns:
        - TreeNode: The tree node.

        """
        if current_node in visited_nodes:
            return None
        visited_nodes.add(current_node)
        node = TreeNode(current_node)

        if self.directed:
            children = [edge.target for edge in graph_edges if edge.source == current_node]
        else:
            children = [edge.target for edge in graph_edges if edge.source == current_node or edge.target == current_node]

        for child in children:
            child_node = self.create_tree(child, graph_edges, visited_nodes)
            if child_node is not None:
                node.add_child(child_node)

        visited_nodes.remove(current_node)
        return node

    def find_node(self, root, parent) -> Optional[TreeNode]:
        """
        Finds a node in the tree.

        Parameters:
        - root: The root of the tree.
        - parent: The parent to find.

        Returns:
        - TreeNode: The node if found, None otherwise.
        """
        if root.value == parent:
            return root
        for child in root.children:
            result = self.find_node(child, parent)
            if result is not None:
                return result
        return None

    def find_parent(self, root, node) -> Optional[TreeNode]:
        """
        Finds the parent of a node in the tree.

        Parameters:
        - root: The root of the tree.
        - node: The node to find the parent of.

        Returns:
        - TreeNode: The parent if found, None otherwise.
        """
        for child in root.children:
            if child.value == node:
                return root
            result = self.find_parent(child, node)
            if result is not None:
                return result
        return None

    def update_tree_recursive(self, root, target_node, graph_edges):
        """
        Updates the tree recursively with the given target node and graph edges.

        Parameters:
        - root: The root of the tree.
        - target_node: The target node to update the tree with.
        - graph_edges: The edges of the graph.

        Returns:
        - TreeNode: The updated tree.
        """
        for child in root.children:
            child.value = self.update_node(child.value, graph_edges)
            self.update_tree_recursive(child, target_node, graph_edges)
        return root

    def update_node(self, value, graph_edges):
        """
        Updates a node with the given graph edges.

        Parameters:
        - value: The value of the node.
        - graph_edges: The edges of the graph.

        Returns:
        - Node: The updated node.
        """
        for edge in graph_edges:
            if edge.source == value:
                return edge.target
        return value