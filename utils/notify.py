from abc import ABC, abstractmethod
from typing import Any

from PIL import Image


class Notify(ABC):
    """Notify class is used to send notifications to the user

    Args:
        ABC (_type_): abc

    Returns:
        _type_: abc
    """
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
