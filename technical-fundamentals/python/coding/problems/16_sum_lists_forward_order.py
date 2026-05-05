# 16. Sum Lists (Forward Order):
# Suppose the digits are stored in forward order. Repeat the above problem.
#
# EXAMPLE
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
# Output: 9 -> 1 -> 2. That is, 912.

from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, value: int, next: Optional["Node"] = None):
        self.value = value
        self.next = next


def sum_lists_forward_order(
    list1: Optional[Node],
    list2: Optional[Node],
) -> Optional[Node]:
    pass
