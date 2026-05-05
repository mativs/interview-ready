# 25. Sort Stack:
# Write a program to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements
# into any other data structure (such as an array).
# The stack supports the following operations: push, pop, peek, and is_empty.

from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class SortStack(Generic[T]):
    def __init__(self):
        pass

    def push(self, value: T) -> None:
        pass

    def pop(self) -> Optional[T]:
        pass

    def peek(self) -> Optional[T]:
        pass

    def is_empty(self) -> bool:
        pass
