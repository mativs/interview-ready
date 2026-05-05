# 10. *Implement a Linked List*
#
# Create the data structure with the corresponding initial functions.

from __future__ import annotations
from typing import TypeVar, Generic, Optional, Callable

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T, next: Optional["Node[T]"] = None):
        self.value = value
        self.next = next


class LinkedList(Generic[T]):
    def __init__(self, head: Optional[Node[T]] = None):
        self.head: Optional[Node[T]] = head
        self.tail: Optional[Node[T]] = head
        self.length: int = 0

    def push(self, value: T) -> None:
        pass

    def filter(self, predicate: Callable[[T], bool]) -> "LinkedList[T]":
        pass

    def visit(self, callback: Callable[[T], None]) -> None:
        pass

    def remove(self, value: T) -> None:
        pass

    def merge(self, other: "LinkedList[T]") -> None:
        pass

    def print(self) -> None:
        pass
