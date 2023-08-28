import torch

from torchvision import transforms  # type: ignore
import torchvision
from torch.utils.data import DataLoader
from PIL import Image
from pathlib import Path

TRANSFORMER = transforms.Compose(
    [
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
    ]
)


def load_dataset(root_path: Path) -> DataLoader:
    return DataLoader(
        torchvision.datasets.ImageFolder(root=root_path, transform=TRANSFORMER),
        batch_size=4,
        shuffle=True,
    )


def load_image(image: Path | bytes | Image.Image) -> torch.Tensor:
    if isinstance(image, Image.Image):
        image = image.convert("RGB")
    else:
        image = Image.open(image).convert("RGB")
    return TRANSFORMER(image).unsqueeze(0)
