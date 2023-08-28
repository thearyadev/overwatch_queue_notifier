from PIL import Image

import torch
from model import NeuralNetwork
from utils.dataset_processor import TRANSFORMER


model = NeuralNetwork()
model.load_state_dict(torch.load("model.pth"))
model.eval()

image = TRANSFORMER(Image.open("./test2.png").convert("RGB"))

with torch.no_grad():
    output = model(image.unsqueeze(0))
    x, predicted = torch.max(output, 1)

classnames = ["noqueue", "queue"]
print(classnames[predicted.item()])
