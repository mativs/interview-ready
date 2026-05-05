# 17. Palindrome:
# Implement a function to check if a linked list is a palindrome.

from __future__ import annotations
from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T, next: Optional["Node[T]"] = None):
        self.value = value
        self.next = next


def is_palindrome(head: Optional[Node[T]]) -> bool:
    pass
