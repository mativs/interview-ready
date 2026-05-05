# 30. Write the basic tree algorithms of Depth-First Search and Breadth-First Search.

from __future__ import annotations
from typing import TypeVar, Generic, Optional, Callable

T = TypeVar("T")


class TreeNode(Generic[T]):
    def __init__(
        self,
        value: T,
        left: Optional["TreeNode[T]"] = None,
        right: Optional["TreeNode[T]"] = None,
        parent: Optional["TreeNode[T]"] = None,
    ):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


class Tree(Generic[T]):
    def bfs(
        self,
        node: Optional[TreeNode[T]],
        visit: Callable[[TreeNode[T]], None],
    ) -> None:
        pass

    def dfs(
        self,
        node: Optional[TreeNode[T]],
        visit: Callable[[TreeNode[T]], None],
    ) -> None:
        pass
