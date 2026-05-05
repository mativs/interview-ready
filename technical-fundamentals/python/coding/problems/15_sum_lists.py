# 15. Sum Lists:
# You have two numbers represented by a linked list, where each node contains a
# single digit. The digits are stored in reverse order, such that the 1's digit is
# at the head of the list. Write a function that adds the two numbers and returns
# the sum as a linked list.
#
# EXAMPLE
# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.

from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, value: int, next: Optional["Node"] = None):
        self.value = value
        self.next = next


def sum_lists(
    list1: Optional[Node],
    list2: Optional[Node],
) -> Optional[Node]:
    pass
