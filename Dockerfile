FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0 ffmpeg wget && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip \
    && pip install deepface tf-keras fastapi uvicorn onnxruntime pillow

RUN mkdir -p /root/.deepface/weights && \
    wget -O /root/.deepface/weights/arcface_weights.h5 https://github.com/serengil/deepface_models/releases/download/v1.0/arcface_weights.h5

EXPOSE 8000

CMD ["uvicorn", "api_rostos:app", "--host", "0.0.0.0", "--port", "8000"]