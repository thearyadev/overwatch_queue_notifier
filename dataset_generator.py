from PIL import Image

from utils.augmentor import Augmentor
from pathlib import Path
import os
from typing import Callable
from uuid import uuid4

sources: tuple[Path, Path] = (
    Path("data/source/noqueue"),
    Path("data/source/queue"),
)
destinations: tuple[Path, Path] = (
    Path("data/train/noqueue"),
    Path("data/train/queue"),
)


def crop(box: tuple[int, int, int, int]) -> Callable[[Image.Image], Image.Image]:
    def inner(
        image: Image.Image,
    ):
        return image.crop(box)

    return inner


for source, destination in zip(sources, destinations):
    image_names = os.listdir(source)
    for image_name in image_names:
        image_path = source / image_name
        image = Image.open(image_path)
        augmentor = (
            Augmentor(image, destination=destination)
            .add(crop((600, 0, 1300, 200)))
            .add(crop((725, 0, 1300, 200)))
            .add(crop((725, 0, 1100, 300)))
        )
        augmentor.apply()
