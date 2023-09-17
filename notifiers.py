from typing import Any

from PIL.Image import Image

from utils.notify import Notify


class SampleNotifier(Notify):
    def send(self, image: Image, **_: Any) -> bool:
        print("Notifier is working")
        return True


# Add a new notifier here
