# 14. Partition:
# Write code to partition a linked list around a value x, such that all nodes less
# than x come before all nodes greater than or equal to x. If x is contained within
# the list, the values of x only need to be after the elements less than x.
# The partition element x can appear anywhere in the "right partition".
#
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition=5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

from __future__ import annotations
from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T, next: Optional["Node[T]"] = None):
        self.value = value
        self.next = next


def partition(head: Optional[Node[T]], x: T) -> Optional[Node[T]]:
    pass
