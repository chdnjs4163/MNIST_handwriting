import os
import io
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps # ImageOps 추가

app = Flask(__name__)

# --- 모델 로드 ---
MODEL_PATH = os.environ.get("MODEL_PATH", "model.weights.h5")
print(f"Loading model from {MODEL_PATH} ...")
model = tf.keras.models.load_model(MODEL_PATH)
_ = model.predict(np.zeros((1, 28, 28, 1), dtype=np.float32))
print("Model loaded successfully.")

# ## 수정된 부분 ##
# 올바른 이미지 전처리 함수
def preprocess_image(image_file):
    """
    사용자가 그린 이미지(흰 배경, 검은 글씨)를
    MNIST 데이터 형식(검은 배경, 흰 글씨)에 맞게 전처리합니다.
    """
    # 이미지를 흑백(Grayscale)으로 불러옵니다.
    img = Image.open(image_file.stream).convert('L')
    
    # 1. 색상 반전 (가장 중요한 부분!)
    # 흰색(255) -> 검은색(0), 검은색(0) -> 흰색(255)
    img = ImageOps.invert(img)
    
    # 2. 28x28 크기로 리사이즈
    img = img.resize((28, 28))
    
    # 3. 이미지를 numpy 배열로 변환하고 0~1 사이로 정규화
    img_array = np.array(img).astype('float32') / 255.0
    
    # 4. 모델이 받을 수 있는 최종 형태로 차원 확장 (1, 28, 28, 1)
    return img_array.reshape(1, 28, 28, 1)


@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "no file"}), 400
    
    try:
        f = request.files["file"]
        arr = preprocess_image(f)
        pred = model.predict(arr, verbose=0)[0]
        
        digit = int(np.argmax(pred))
        probability = float(np.max(pred))
        all_probabilities = [float(p) for p in pred]
        
        return jsonify({
            "digit": digit,
            "prob": probability,
            "probabilities": all_probabilities 
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # 필요한 라이브러리: pip install flask tensorflow numpy Pillow
    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=False)