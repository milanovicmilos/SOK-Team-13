from typing import Any


class Node:

    def __init__(self, node_id: str, data: Any):
        self._node_id = node_id
        self._data = data

    @property
    def node_id(self) -> str:
        return self._node_id

    @property
    def data(self) -> Any:
        return self._data


