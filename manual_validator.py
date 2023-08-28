from PIL import Image

import torch
from model import NeuralNetwork
from utils.dataset_processor import load_image
from pathlib import Path


model = NeuralNetwork()
model.load_state_dict(torch.load("./model/model.pth"))
model.eval()

image = load_image(Path("./test4.png"))

with torch.no_grad():
    output = model(image)
    x, predicted = torch.max(output, 1)

classnames = ["noqueue", "queue"]
print(classnames[predicted.item()])
