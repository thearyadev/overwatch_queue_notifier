import torch
import torch.nn as nn
import torch.nn.functional as F


class NeuralNetwork(nn.Module):
    """ Neural Network for classification
    """
    def __init__(self) -> None:
        super(NeuralNetwork, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, 3)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(16 * 15 * 15, 128) 
        self.fc2 = nn.Linear(128, 2) # 2 classes

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.pool(F.relu(self.conv1(x)))
        x = x.view(-1, 16 * 15 * 15)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
