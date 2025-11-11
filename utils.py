import numpy as np
from PIL import Image, ImageOps

def preprocess_image(file_obj):
    img = Image.open(file_obj).convert("L") # 그레이스케일
    img = ImageOps.invert(img)
    img = ImageOps.pad(img, (28, 28), method=Image.BILINEAR, color=255, centering=(0.5, 0.5))
    arr = np.array(img).astype("float32") / 255.0
    arr = arr.reshape(1, 28, 28, 1)
    return arr

def postprocess(pred):
    prob = float(pred.max())
    cls = int(pred.argmax())
    return {"digit": cls, "prob": prob}