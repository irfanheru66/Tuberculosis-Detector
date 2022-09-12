FROM python:3.9.12-slim

WORKDIR /app

RUN apt-get update

RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

RUN pip3 install gdown

RUN pip3 install streamlit

RUN pip3 install onnxruntime
#onnx
RUN gdown --fuzzy https://drive.google.com/file/d/1--Nk3-4zXsPVsZoid162ozujyWXrdu9V/view?usp=sharing
#.pt
RUN gdown --fuzzy https://drive.google.com/file/d/10ByzNWVz-Vtg0qhIG4tO5ASfhmN0QhRu/view?usp=sharing

COPY . .

CMD streamlit run app.py