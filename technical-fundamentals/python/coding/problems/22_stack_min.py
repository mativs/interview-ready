# 22. Stack Min:
# How would you design a stack which, in addition to push and pop, has a function
# min which returns the minimum element?
# Push, pop, and min should all operate in O(1) time.

from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class StackMin(Generic[T]):
    def __init__(self):
        pass

    def push(self, value: T) -> None:
        pass

    def pop(self) -> Optional[T]:
        pass

    def min(self) -> Optional[T]:
        pass
