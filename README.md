✍️ AI 손글씨 숫자 인식 웹 서비스 (MNIST)

머신러닝 딥러닝 모델을 이용해 실시간으로 손글씨 숫자를 예측하는 풀스택(Full-Stack) 웹 애플리케이션입니다.

사용자가 웹 캔버스에 직접 손글씨 숫자를 그리면, 서버에 탑재된 CNN 딥러닝 모델이 이를 인식하고 예측 결과를 반환합니다. 예측된 숫자뿐만 아니라, 각 숫자에 대한 예측 확률을 `Chart.js`를 이용한 막대그래프로 시각화하여 제공합니다.


🖥️ 실행 화면 (Screenshot)
<img width="980" height="542" alt="image" src="https://github.com/user-attachments/assets/062719d8-774b-4a21-ae53-b6e4eaaa6618" />

<br>

✨ 주요 기능

✅ 실시간 손글씨 숫자 예측: 캔버스에 마우스로 숫자를 그리면, `Flask` 서버에 탑재된 `TensorFlow/Keras CNN` 모델이 즉시 품종을 예측하여 결과와 이미지를 보여줍니다.

✅ 직관적인 예측 확률 시각화: 0부터 9까지 모든 숫자에 대한 예측 확률을 `Chart.js`를 활용한 동적 막대그래프로 제공하여, 모델의 '고민' 과정을 시각적으로 보여줍니다.

✅ HTML5 Canvas 기반 드로잉: 마우스와 터치 이벤트를 지원하는 캔버스에서 사용자가 자유롭게 숫자를 그릴 수 있으며, 펜 굵기 조절 및 캔버스 초기화('지우기') 기능을 제공하여 사용자 편의성을 높였습니다.

✅ 비동기 API 통신: `JavaScript`의 `fetch API`를 사용하여 페이지 새로고침 없이 캔버스 이미지를 서버(Python Flask)와 비동기 방식으로 통신합니다.

✅ 서버 사이드 이미지 전처리: 사용자가 그린 이미지(흰 배경, 검은 글씨)를 모델이 학습한 MNIST 데이터(검은 배경, 흰 글씨, 28x28) 형식에 맞게 색상 반전, 리사이징, 정규화를 서버 측에서 자동 수행합니다.

<br>

🛠️ 아키텍처 구조

프로젝트의 전체 데이터 흐름도입니다. 클라이언트(브라우저)에서 사용자 입력이 어떻게 서버(Flask)로 전달되고, AI 모델을 거쳐 처리된 후, 다시 클라이언트에 시각화되는지 명확하게 보여줍니다.

<img width="396" height="708" alt="image" src="https://github.com/user-attachments/assets/24ffd933-2460-4c25-bccc-588a9055fb19" />
<br>

### 📈 데이터 흐름 상세 설명
1. [Client] 사용자 입력: 사용자가 `HTML5 Canvas`에 손글씨 숫자를 그립니다.
2. [Client] 이미지 변환: `JavaScript`가 '예측하기' 버튼 클릭을 감지하고, 캔버스 내용을 **PNG 이미지 데이터**로 변환합니다.
3. [API 요청]: `JavaScript (fetch API)`가 변환된 PNG 이미지를 Flask 서버의 `/predict` 엔드포인트로 **POST 요청**으로 전송합니다.
4. [Server] 요청 처리: `Flask` 서버의 라우트(`Flask Route`)가 요청을 받습니다.
5. [Server] 이미지 로드: `Pillow` 라이브러리가 전송된 PNG 이미지 데이터를 메모리로 로드합니다.
6. [Server] 이미지 전처리: `Preprocessing` 함수를 통해 이미지를 (색상 반전, 28x28 리사이징, 정규화)하여 모델 입력 형식에 맞춥니다.
7. [Server] AI 모델 추론: `TensorFlow/Keras CNN Model`이 전처리된 이미지 데이터를 받아 `model.predict()`를 수행하여 예측 확률을 계산합니다.
8. [API 응답]: `Flask` 서버가 0~9까지 10개 숫자에 대한 예측 확률 리스트를 **JSON 형식**으로 클라이언트에 반환합니다.
9. [Client] 결과 시각화: `JavaScript`가 서버로부터 받은 JSON 응답을 파싱하고, `Chart.js`를 사용하여 예측 확률을 동적인 막대그래프로 화면에 업데이트합니다.

<br>

 ⚙️ 기술 스택 (Tech Stack)

🖥️ Frontend
* HTML5 / CSS3: 웹페이지의 구조(캔버스, 버튼 등)와 디자인을 담당합니다.
* JavaScript (ES6+): 캔버스 드로잉 로직, DOM 조작, `fetch API`를 통한 비동기 서버 통신을 구현합니다.
* HTML5 Canvas: 사용자의 손글씨 입력이 이루어지는 드로잉 영역을 제공합니다.
* Chart.js: AI 모델의 0~9 예측 확률을 직관적인 막대그래프로 시각화합니다.

 🐍 Backend
* Python3: 백엔드 로직의 핵심 프로그래밍 언어입니다.
* Flask: 경량 웹 프레임워크로, AI 모델 서빙을 위한 `/predict` API 엔드포인트를 구축하고 클라이언트 요청을 처리합니다.
* TensorFlow (Keras): 사전 학습된 CNN 모델(`.h5`)을 로드하고, 전처리된 이미지 데이터에 대한 실시간 추론(Inference)을 수행합니다.
* Pillow (PIL): 클라이언트로부터 받은 이미지 데이터를 로드하고, 모델 입력 형식에 맞춰 색상 반전 및 리사이징 등 전처리 작업을 수행합니다.
* Numpy: 이미지 데이터를 TensorFlow/Keras 모델이 처리할 수 있는 다차원 숫자 배열로 변환하는 데 사용됩니다.

<br>

🚀 설치 및 실행 방법

1.  저장소 클론 (Clone)
    ```bash
    git clone [https://github.com/](https://github.com/)[Your-Username]/[Your-Repository-Name].git
    cd [Your-Repository-Name]
    ```

2.  가상 환경 생성 및 활성화 (권장)
    ```bash
    # Python 가상 환경 생성
    python -m venv venv

    가상 환경 활성화 (Windows)
    .\venv\Scripts\activate

    가상 환경 활성화 (macOS/Linux)
    source venv/bin/activate
    ```

3.  필요 라이브러리 설치
    ```bash
    pip install -r requirements.txt
    ```
    (※ `requirements.txt` 파일이 없다면, 다음 명령어를 실행하여 수동 설치: `pip install Flask tensorflow numpy pillow`)

4.  lask 서버 실행
    ```bash
    python app.py
    ```

5.  웹 브라우저 접속
    서버가 실행되면 웹 브라우저를 열고 `http://127.0.0.1:5000` 주소로 접속합니다.

    향후 개선 사항
* 모델 로딩 최적화: 현재 개발 편의상 모델을 실시간으로 학습하거나 매 요청마다 로드하는 방식일 경우, `pickle` 등을 이용해 미리 학습된 모델(`.h5` 파일)을 서버 시작 시 **메모리에 한 번만 로드**하는 방식으로 리팩토링하여 서버 응답 속도를 크게 개선할 수 있습니다.
* 배포 환경 확장: `Docker` 컨테이너를 기반으로 `AWS Lambda`, `Google Cloud Run` 또는 `Kubernetes`와 같은 서버리스(Serverless) 또는 컨테이너 오케스트레이션 환경에 배포하여, 트래픽 변화에 유연하게 대응하고 비용 효율성을 높일 수 있습니다.
