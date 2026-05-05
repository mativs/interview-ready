# 18. Intersection:
# Given two (singly) linked lists, determine if the two lists intersect.
# Return the first intersecting node. Note that the intersection is defined
# based on reference, not value.

from __future__ import annotations
from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T, next: Optional["Node[T]"] = None):
        self.value = value
        self.next = next


def intersection(
    list1: Optional[Node[T]],
    list2: Optional[Node[T]],
) -> Optional[Node[T]]:
    pass
