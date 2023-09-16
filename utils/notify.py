from abc import ABC, abstractmethod
from PIL import Image
from typing import Any


class Notify(ABC):
    @abstractmethod
    def send(self, image: Image.Image, **_: Any) -> bool:
        """Returns True if the notification was sent successfully.
        send method is provided with an image and any additional arguments

        Args:
            image (Image.Image): screenshot

        Returns:
            bool: success state
        """
        return NotImplemented
