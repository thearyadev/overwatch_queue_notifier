from utils.notify import Notify
from typing import Any
from PIL.Image import Image


class SampleNotifier(Notify):
    def send(self, image: Image, **_: Any) -> bool:
        return True


# Add a new notifier here
