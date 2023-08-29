from abc import ABC, abstractmethod


class Notify(ABC):
    @abstractmethod
    def send(self, message):
        pass
