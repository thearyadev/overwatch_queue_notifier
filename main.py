import argparse
import importlib

from utils.notify import Notify
from PIL import Image


def import_notifier(module_str: str, package_str: str) -> Notify:
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


def main(notifier_import_str: str) -> int:
    notifier: Notify = import_notifier(*notifier_import_str.split(":"))
    notifier.send(
        image=Image.open("data/source/noqueue/Screenshot_1.png"),
    )

    while True:
        # Program Mainloop
        break

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--notifier", type=str, required=True)
    args = parser.parse_args()

    raise SystemExit(main(args.notifier))
