from pathlib import Path

import torch
import torchvision
from PIL import Image
from torch.utils.data import DataLoader
from torchvision import transforms

TRANSFORMER = transforms.Compose(
    [
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
    ]
)


def load_dataset(root_path: Path) -> DataLoader[torchvision.datasets.ImageFolder]:
    """Load dataset from a root path

    Args:
        root_path (Path): Path to the dataset

    Returns:
        DataLoader[torchvision.datasets.ImageFolder]: Dataset
    """
    return DataLoader(
        torchvision.datasets.ImageFolder(root=root_path, transform=TRANSFORMER),
        batch_size=4,
        shuffle=True,
    )


def load_image(image: Path | bytes | Image.Image) -> torch.Tensor:
    """Load an image from a path or bytes or PIL.Image.Image and convert it to a tensor

    Args:
        image (Path | bytes | Image.Image): Path to the image or bytes or PIL.Image.Image

    Returns:
        torch.Tensor: Tensor representation of the image
    """
    if isinstance(image, Image.Image):
        image = image.convert("RGB")
    else:
        image = Image.open(image).convert("RGB")
    # apply transformations to the image
    return TRANSFORMER(image).unsqueeze(0)  # type: ignore
