import io
from pathlib import Path
from time import perf_counter

import torch
from PIL import Image

from model import NeuralNetwork
from utils.dataset_processor import load_image

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = NeuralNetwork().to(device)
model.load_state_dict(torch.load("./model/model.pth", map_location=device))
model.eval()
with open("./test5.png", "rb") as f:
    b = io.BytesIO(f.read())

with torch.no_grad():
    start = perf_counter()
    for i in range(100):
        image = load_image(b).to(device)  # type: ignore
        output = model(image)
        x, predicted = torch.max(output, 1)
        classes = ("noqueue", "queue")
        print(classes[predicted[0]])
        exit()
    end = perf_counter()
    rate = 100 / (end - start)
    print(f"Rate: {rate} images/sec")
