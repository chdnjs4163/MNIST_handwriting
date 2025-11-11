🤖 AI 손글씨 숫자 인식 웹 (MNIST)

웹 브라우저의 캔버스에 숫자를 그리면, AI 모델이 실시간으로 예측해주는 간단한 웹 서비스입니다.
예측 결과는 0부터 9까지 각 숫자에 대한 확률을 막대그래프로 보여줍니다.

🖥️ 실행 화면
<img width="980" height="542" alt="image" src="https://github.com/user-attachments/assets/16793f60-848b-459a-b4ec-8318764ac268" />

 📌 주요 기능

* **실시간 예측**: 캔버스에 그린 숫자를 `Flask` 서버로 전송하여 `TensorFlow` 모델이 즉시 예측합니다.
* **비동기 통신**: 페이지 새로고침 없이 `JavaScript (fetch)`를 이용해 서버와 통신합니다.
* **확률 시각화**: `Chart.js`를 사용해 0~9까지 모든 숫자의 예측 확률을 막대그래프로 보여줍니다.
* **드로잉 도구**: `HTML5 Canvas`와 JS로 숫자 그리기, 펜 굵기 조절, 지우기 기능을 구현했습니다.

🛠️ 사용 기술

* **Front-end**: HTML, CSS, JavaScript (Canvas, Chart.js)
* **Back-end**: Python, Flask, TensorFlow (Keras)
* **이미지 처리**: Pillow, Numpy

🚀 실행 방법

1.  프로젝트 클론
    ```bash
    git clone [https://github.com/](https://github.com/)[본인_GitHub_ID]/[저장소_이름].git
    cd [저장소_이름]
    ```

2.  가상환경 만들고 실행
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  필요한 패키지 설치
    ```bash
    pip install -r requirements.txt
    ```
    (※ `requirements.txt` 파일이 없다면 `pip install Flask tensorflow numpy pillow`를 실행하세요.)

4.  서버 실행
    ```bash
    python app.py
    ```

5.  브라우저에서 확인
    * 웹 브라우저에서 `http://127.0.0.1:5000` 주소로 접속합니다.
