import argparse
import importlib

from utils.notify import Notify
from utils.dataset_processor import load_image
from PIL import Image
from model import NeuralNetwork
import torch
import io


def import_notifier(module_str: str, package_str: str) -> Notify:
    """Imports a module from a string. Raises TypeError if the module is not a subclass of Notify

    Args:
        module_str (str): String of the module
        package_str (str): String of the package

    Raises:
        TypeError: If the module is not a subclass of Notify
        TypeError: If the module does not implement all abstract methods

    Returns:
        Notify: Notifier
    """
    module = importlib.import_module(module_str)
    try:
        notifier: Notify = getattr(
            module, package_str
        )()  # attempt to initialize the class
    except TypeError:  # if the abstract methods are not implemented
        # exception is raised from ABC's
        raise TypeError(
            f"Notifier must be a subclass of Notify and must implement all abstract methods. See notifiers.py for more info. Unable to instanciate abstract class "
        )
    if not isinstance(notifier, Notify):  # if the class is not a subclass of Notify
        raise TypeError(
            "Notifier must be a subclass of Notify and must implement all abstract methods. See notifiers.py for more info."
        )
    return notifier


def screenshot() -> Image.Image:
    """Gets a screenshot of Overwatch

    Returns:
        Image.Image: screenshot
    """
    return NotImplemented


def crop(image: Image.Image, box: tuple[int, int, int, int]) -> Image.Image:
    """Crops the full screenshot to the given box

    Args:
        image (Image.Image): full screenshot
        box (tuple[int, int, int, int]): box to crop

    Returns:
        Image.Image: cropped image
    """
    return image.crop(box)


def in_queue(image: Image.Image, model: NeuralNetwork, device: torch.device) -> bool:
    """ Uses the pytorch model to predict if the image is in queue or not

    Args:
        image (Image.Image): input image (should be cropped to the queue box)
        model (NeuralNetwork): pytorch model in eval mode
        device (torch.device): device to run the model on

    Returns:
        bool: True if the image is in queue, False otherwise
    """
    # this code was ugly (visually) so i decided to shrink it.
    # @future_human, if you are reading this, enjoy debugging
    with torch.no_grad():
        if ("noqueue", "queue")[
            torch.max(model(load_image(image).to(device)), 1)[0]
        ] == "queue":
            return True
        return False


def main(notifier_import_str: str) -> int:
    """Main function

    Args:
        notifier_import_str (str): Import string for the notifier

    Returns: Exit code
    """
    notifier: Notify = import_notifier(*notifier_import_str.split(":"))
    notifier.send(
        image=Image.open("data/source/noqueue/Screenshot_1.png"),
    )
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model: NeuralNetwork = NeuralNetwork()
    model.load_state_dict(torch.load("./model/model.pth", map_location=device))
    model.eval()

    while True:
        # Program Mainloop
        break

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--notifier", type=str, required=True)
    args = parser.parse_args()

    raise SystemExit(main(args.notifier))
