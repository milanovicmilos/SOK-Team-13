class Edge:

    def __init__(self, source_node: Node, target_node: Node):
        self._source_node = source_node
        self._target_node = target_node

    @property
    def source_node(self):
        return self._source_node

    @property
    def target_node(self):
        return self._target_node
