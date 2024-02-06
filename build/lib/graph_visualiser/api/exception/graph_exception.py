class GraphException(Exception):
    """Custom exception class for graph-related errors."""

    def __init__(self, message="Graph exception occurred"):
        self.message = message
        super().__init__(self.message)
