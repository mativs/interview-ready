# 19. Loop Detection:
# Given a circular linked list, implement an algorithm that returns the node
# at the beginning of the loop.
#
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer
# points to an earlier node, so as to make a loop in the linked list.
#
# EXAMPLE
# Input: A->B->C->D->E->C [the same C as earlier]
# Output: C

from __future__ import annotations
from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T, next: Optional["Node[T]"] = None):
        self.value = value
        self.next = next


def detect_loop(head: Optional[Node[T]]) -> Optional[Node[T]]:
    pass
