import cv2
from PIL import Image

import torch
from model import NeuralNetwork
from utils.dataset_processor import load_image
from pathlib import Path
from time import perf_counter
import io
from utils.dataset_processor import TRANSFORMER


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = NeuralNetwork().to(device)
model.load_state_dict(torch.load("./model/model.pth", map_location=device))
model.eval()

with torch.no_grad():
    cap = cv2.VideoCapture("clip.mp4")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("frame", frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = TRANSFORMER(
            Image.fromarray(frame).convert("RGB").crop((600, 0, 1300, 100))
        ).unsqueeze(0)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        output = model(image)
        x, predicted = torch.max(output, 1)
        classes = ("noqueue", "queue")
        print(f"CURRENT STATE: {classes[predicted[0]]}")

    cap.release()
    cv2.destroyAllWindows()
