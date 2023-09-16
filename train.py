import argparse
from pathlib import Path

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from model import NeuralNetwork
from utils.dataset_processor import TRANSFORMER, load_dataset


def main(
    epochs: int,
    save: bool = False,
) -> int:
    train = load_dataset(Path("data/train"))
    test = load_dataset(Path("data/test"))
    classes = ("noqueue", "queue")

    network = NeuralNetwork()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(network.parameters(), lr=0.001, momentum=0.9)

    for epoch in range(epochs):
        running_loss = 0.0
        for i, data in enumerate(train, 0):
            inputs, labels = data
            optimizer.zero_grad()
            outputs = network(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            if i % 10 == 0:
                print("[%d, %5d] loss: %.3f" % (epoch + 1, i + 1, running_loss / 2000))
                running_loss = 0.0
    total = 0
    correct = 0

    with torch.no_grad():
        for data in test:
            images, labels = data
            outputs = network(images)
            _, predicted = torch.max(outputs.data, 1)
            print(
                "Predicted: ", " ".join("%5s" % classes[predicted[j]] for j in range(2))
            )
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(f"Accuracy: {100 * correct / total}%")

    if save:
        torch.save(network.state_dict(), "model.pth")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", type=int, default=10)
    args = parser.parse_args()
    raise SystemExit(main(save=True, epochs=10))
