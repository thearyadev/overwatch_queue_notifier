from typing import Generic, TypeVar, Dict

T = TypeVar("T")


class AutoDropStack(Generic[T]):
    def __init__(self, max_size: int):
        self.max_size = max_size
        self._stack: list[T] = []

    @property
    def stack(self) -> list[T]:
        return self._stack

    def push(self, item: T):
        if len(self._stack) >= self.max_size:
            self._stack.pop(0)
        self._stack.append(item)

    def percentiles(self) -> Dict[T, float]:
        return {
            item: self._stack.count(item) / len(self._stack) for item in self._stack
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
