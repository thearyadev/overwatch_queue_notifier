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


if __name__ == "__main__":
    s = AutoDropStack(5)  # type: ignore
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)
    s.push(8)
    print(s.percentiles())
