# 39. BST Sequences:
# A binary search tree was created by traversing through an array from left to right
# and inserting each element. Given a binary search tree with distinct elements,
# print all possible arrays that could have led to this tree.
#
# EXAMPLE
# Input:
#       2
#      / \
#     1   3
# Output: [[2, 1, 3], [2, 3, 1]]

from __future__ import annotations
from typing import TypeVar, Generic, Optional, List

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


def bst_sequences(root: TreeNode[T]) -> List[List[T]]:
    pass
