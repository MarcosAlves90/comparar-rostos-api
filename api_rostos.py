import os
import warnings
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from deepface import DeepFace
import base64
import uuid

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings('ignore')

app = FastAPI()

def salvar_base64_para_arquivo(base64_str, pasta_temp="temp_imgs"):
    if not os.path.exists(pasta_temp):
        os.makedirs(pasta_temp)
    nome_arquivo = f"{uuid.uuid4()}.jpg"
    caminho = os.path.join(pasta_temp, nome_arquivo)
    try:
        conteudo = base64.b64decode(base64_str, validate=True)
    except Exception as e:
        raise ValueError(f"Base64 inválido: {e}")
    with open(caminho, "wb") as f:
        f.write(conteudo)
    return caminho


class ImagensRequest(BaseModel):
    imagem1: str  # base64
    imagem2: str  # base64

@app.get("/", response_class=FileResponse)
def home():
    return FileResponse("static/index.html")


@app.post("/comparar-rostos")
async def comparar_rostos(imagens: ImagensRequest):
    """
    Recebe dois base64 de imagem via JSON e compara os rostos.
    """
    caminho1 = caminho2 = None
    try:
        caminho1 = salvar_base64_para_arquivo(imagens.imagem1)
        caminho2 = salvar_base64_para_arquivo(imagens.imagem2)
        resultado = DeepFace.verify(
            caminho1,
            caminho2,
            model_name="ArcFace",
            enforce_detection=False
        )
        return {
            "resultado": resultado["verified"],
            "distancia": resultado.get("distance", None)
        }
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if caminho1 and os.path.exists(caminho1):
            os.remove(caminho1)
        if caminho2 and os.path.exists(caminho2):
            os.remove(caminho2)
