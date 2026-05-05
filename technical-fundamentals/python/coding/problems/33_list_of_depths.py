# 33. List of Depths:
# Given a binary tree, design an algorithm which creates a linked list of all the
# nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

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


class ListNode(Generic[T]):
    def __init__(self, value: T, next: Optional["ListNode[T]"] = None):
        self.value = value
        self.next = next


def list_of_depths(root: Optional[TreeNode[T]]) -> List[ListNode[T]]:
    pass
