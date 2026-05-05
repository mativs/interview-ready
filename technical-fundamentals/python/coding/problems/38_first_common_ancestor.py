# 38. First Common Ancestor:
# Design an algorithm and write code to find the first common ancestor of two nodes
# in a binary tree. Avoid storing additional nodes in a data structure.
# NOTE: This is not necessarily a binary search tree.

from __future__ import annotations
from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class TreeNode(Generic[T]):
    def __init__(
        self,
        value: T,
        left: Optional["TreeNode[T]"] = None,
        right: Optional["TreeNode[T]"] = None,
    ):
        self.value = value
        self.left = left
        self.right = right


def first_common_ancestor(
    root: Optional[TreeNode[T]],
    p: TreeNode[T],
    q: TreeNode[T],
) -> Optional[TreeNode[T]]:
    pass
