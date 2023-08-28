from __future__ import annotations

from PIL import Image
from typing import Callable
from pathlib import Path
from uuid import uuid4


class Augmentor:
    def __init__(self, image: Image.Image, destination: Path):
        self.image = image
        self.process: list[Callable[[Image.Image], Image.Image]] = list()
        self.destination = destination

    def add(self, func: Callable[[Image.Image], Image.Image]) -> Augmentor:
        self.process.append(func)
        return self

    def apply(self):
        for func in self.process:
            func(self.image).save(self.destination / f"{uuid4()}.png")
