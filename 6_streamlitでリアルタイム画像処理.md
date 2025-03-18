# **リアルタイム画像処理アプリを作成してみよう**
## **リアルタイム画像処理Webアプリを作成**
### **ライブラリをインストールする**
```
pip install -U streamlit streamlit-webrtc opencv-python-headless
```
- `streamlit`: Streamlit本体
- `streamlit-webrtc`: Streamlitでリアルタイム映像・音声を扱うコンポーネント
- `opencv-python-headless`: OpenCV(UIはStreamlitで作成するのでHeadless版を使用)

### **カメラの映像を表示するWebアプリを作成**

- 以下の内容を`camera.py`として作成し、保存する
  ```python
  import streamlit as st
  from streamlit_webrtc import webrtc_streamer

  st.title("My first Streamlit app")
  st.write("Hello, world")

  webrtc_streamer(key="example")
  ```

- プログラムを実行する
  ```sh
  streamlit run camera.py
  ```

- プログラムを停止する
  `Ctrl + c`


### **リアルタイム画像処理を行うWebアプリの作成**

- 以下の内容を`webrtc.py`として作成し、保存する
  ```python
  import streamlit as st
  from streamlit_webrtc import webrtc_streamer
  import av
  import cv2

  st.title("My first Streamlit app")
  st.write("Hello, world")

  def callback(frame):
      img = frame.to_ndarray(format="bgr24")
      img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)

      return av.VideoFrame.from_ndarray(img, format="bgr24")

  webrtc_streamer(key="example", video_frame_callback=callback)
  ```

- プログラムを実行する
  ```sh
  streamlit run webrtc.py
  ```

- プログラムを停止する
  `Ctrl + c`
