# 11. Remove Dups:
# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed?
#
# 1 -> 2 -> 2 -> 2 -> 4

from __future__ import annotations
from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T, next: Optional["Node[T]"] = None):
        self.value = value
        self.next = next


def remove_dups(head: Optional[Node[T]] = None) -> Optional[Node[T]]:
    pass
