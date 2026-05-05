# 24. Queue via Stacks:
# Implement a MyQueue class which implements a queue using two stacks.

from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class MyQueue(Generic[T]):
    def __init__(self):
        pass

    def enqueue(self, value: T) -> None:
        pass

    def dequeue(self) -> Optional[T]:
        pass

    def peek(self) -> Optional[T]:
        pass

    def is_empty(self) -> bool:
        pass
