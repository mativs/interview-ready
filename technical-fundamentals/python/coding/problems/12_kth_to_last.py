# 12. Return Kth to Last:
# Implement an algorithm to find the kth to last element of a singly linked list.

from __future__ import annotations
from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T, next: Optional["Node[T]"] = None):
        self.value = value
        self.next = next


def kth_to_last(head: Node[T], k: int) -> Optional[Node[T]]:
    pass
