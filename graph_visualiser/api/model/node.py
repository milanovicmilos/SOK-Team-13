from typing import Any


class Node:

    def __init__(self, node_id: int, data: dict[str, Any]):
        self._node_id = node_id
        self._data = data

    @property
    def node_id(self) -> int:
        return self._node_id

    @property
    def data(self) -> dict[str, Any]:
        return self._data

