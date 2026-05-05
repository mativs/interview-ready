# 31. Route Between Nodes:
# Given a directed graph, design an algorithm to find out whether there is a route
# between two nodes.

from __future__ import annotations
from typing import List


class GraphNode:
    def __init__(self, value: int, neighbors: List["GraphNode"] = None):
        self.value = value
        self.neighbors: List["GraphNode"] = neighbors if neighbors is not None else []


def has_route_between_nodes(start: GraphNode, end: GraphNode) -> bool:
    pass
