FROM python:3.11-slim

# Instala dependências do sistema necessárias para o DeepFace
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0 ffmpeg && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip \
    && pip install deepface tf-keras fastapi uvicorn onnxruntime pillow

EXPOSE 8000

CMD ["uvicorn", "api_rostos:app", "--host", "0.0.0.0", "--port", "8000"]