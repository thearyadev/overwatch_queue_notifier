from typing import Dict, Generic, TypeVar

T = TypeVar("T")


class AutoDropStack(Generic[T]):
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.__stack: list[T] = []

    @property
    def stack(self) -> list[T]:
        return self.__stack

    def push(self, item: T):
        if len(self.__stack) >= self.max_size:
            self.__stack.pop(0)
        self.__stack.append(item)

    def percentiles(self) -> Dict[T, float]:
        return {
            item: self.__stack.count(item) / len(self.__stack) for item in self.__stack
        }
