import argparse
import importlib

from utils.notify import Notify


def main(notifier_module_name: str, notifier_package_name: str) -> int:
    module = importlib.import_module(notifier_module_name)
    notifier = getattr(module, notifier_package_name)()
    notifier.send("Hello World")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--notifier", type=str, required=True)
    args = parser.parse_args()

    raise SystemExit(main(args.notifier.split(":")[0], args.notifier.split(":")[1]))
