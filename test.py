# from PIL import Image

# import torch
# import torch.nn as nn

# from torchvision import transforms
# from torch.functional import F


# model = Net()
# model.load_state_dict(torch.load("model.pth"))
# model.eval()

# transform = transforms.Compose(
#     [
#         transforms.Resize((32, 32)),
#         transforms.ToTensor(),
#         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
#     ]
# )
# image = Image.open(
#     "data/test/noqueue/1bdccdab-eb92-469e-ab7a-f110e6e11457.png"
# ).convert("RGB")

# image = transform(image)
# print(image.shape)
# with torch.no_grad():
#     output = model(image.unsqueeze(0))
#     print(output)
#     x, predicted = torch.max(output, 1)
#     print(predicted)
#     print(x)

# classnames = ["noqueue", "queue"]
# print(classnames[predicted.item()])
