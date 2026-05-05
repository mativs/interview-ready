# 35. Validate BST:
# Implement a function to check if a binary tree is a binary search tree.

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


def validate_bst(node: Optional[TreeNode[T]]) -> bool:
    pass
