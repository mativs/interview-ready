# 23. Stack of Plates:
# Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack
# exceeds some threshold. Implement a data structure SetOfStacks that mimics this.
# SetOfStacks should be composed of several stacks and should create a new stack once
# the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should
# behave identically to a single stack.
#
# FOLLOW UP: Implement a function pop_at(index) which performs a pop on a specific sub-stack.

from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class StackOfPlates(Generic[T]):
    def __init__(self, capacity: int):
        pass

    def push(self, value: T) -> None:
        pass

    def pop(self) -> Optional[T]:
        pass
