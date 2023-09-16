from __future__ import annotations

from pathlib import Path
from typing import Callable
from uuid import uuid4

from PIL import Image


class Augmentor:
    """Augmentor class is used to apply a series of functions to an image and save the result to a destination folder.
    """
    def __init__(self, image: Image.Image, destination: Path):
        """

        Args:
            image (Image.Image): Source image
            destination (Path): Destination folder
        """
        self.image = image
        self.process: list[Callable[[Image.Image], Image.Image]] = list() # list of callables to run on the image
        self.destination = destination

    def add(self, func: Callable[[Image.Image], Image.Image]) -> Augmentor:
        """ Add a function to the process list

        Args:
            func (Callable[[Image.Image], Image.Image]): Function to be added to the process list

        Returns:
            Augmentor: self
        """
        self.process.append(func)
        return self

    def apply(self) -> None:
        """ Apply all the functions in the process list to the image and save the result to the destination folder
        """
        for func in self.process:
            func(self.image).save(self.destination / f"{uuid4()}.png")
