# 21. Three in One:
# Describe how you could use a single array to implement three stacks.

from typing import TypeVar, Generic, Optional, List

T = TypeVar("T")


class ThreeStacks(Generic[T]):
    def __init__(self, array_length: int):
        pass

    def push(self, stack_num: int, value: T) -> None:
        pass

    def pop(self, stack_num: int) -> Optional[T]:
        pass

    def peek(self, stack_num: int) -> Optional[T]:
        pass
