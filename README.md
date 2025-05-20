# Comparador de Rostos com FastAPI e DeepFace

![GitHub repo size](https://img.shields.io/github/repo-size/MarcosAlves90/comparar-rostos-api?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/MarcosAlves90/comparar-rostos-api?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/MarcosAlves90/comparar-rostos-api?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/MarcosAlves90/comparar-rostos-api?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/MarcosAlves90/comparar-rostos-api?style=for-the-badge)
![GitHub License](https://img.shields.io/github/license/MarcosAlves90/comparar-rostos-api?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/MarcosAlves90/comparar-rostos-api?style=for-the-badge)
![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red?style=for-the-badge)

Este projeto é uma API para comparar a semelhança entre dois rostos em imagens, utilizando o framework FastAPI e a biblioteca DeepFace. A aplicação recebe duas imagens em formato base64, realiza a comparação facial e retorna se os rostos são semelhantes, além da distância de similaridade.

## Funcionalidades

- **Comparação de rostos:** Recebe duas imagens e verifica se os rostos são semelhantes.
- **Interface web simples:** Frontend em HTML/Tailwind para upload e visualização do resultado.
- **API REST:** Endpoint para integração com outros sistemas.
- **Execução via Docker:** Pronto para rodar em container.

## Tecnologias Utilizadas

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![DeepFace](https://img.shields.io/badge/DeepFace-4B8BBE?style=for-the-badge&logo=python&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-222c37?style=for-the-badge&logo=uvicorn)
![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=yellow)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

- [FastAPI](https://fastapi.tiangolo.com/)
- [DeepFace](https://github.com/serengil/deepface)
- [Uvicorn](https://www.uvicorn.org/)
- [Python 3.11](https://www.python.org/)
- [Docker](https://www.docker.com/)

## Como Executar Localmente

### 1. Pré-requisitos

- Python 3.11+
- pip
- (Opcional) Docker

### 2. Instalação sem Docker

```bash
pip install deepface tf-keras fastapi uvicorn onnxruntime pillow
```

### 3. Executando a API

```bash
uvicorn api_rostos:app --reload
```

Acesse: [http://localhost:8000](http://localhost:8000)

### 4. Executando com Docker

```powershell
docker build -t comparador-rostos .
docker run -p 8000:8000 comparador-rostos
```

Acesse: [http://localhost:8000](http://localhost:8000)

## Como Usar

1. Abra a interface web em `/` (raiz do servidor).
2. Faça upload de duas imagens (JPG, PNG, etc).
3. Clique em "Comparar Rostos".
4. Veja o resultado na tela, incluindo se os rostos são semelhantes e a distância calculada.

## Estrutura dos Arquivos

- `api_rostos.py`: Código principal da API.
- `static/index.html`: Interface web para upload e comparação.
- `Dockerfile`: Configuração para execução em container.
- `temp_imgs/`: Pasta temporária para imagens recebidas (criada automaticamente).

## Endpoints da API

### `POST /comparar-rostos`

Recebe um JSON com duas imagens em base64:

```json
{
  "imagem1": "<base64 da imagem 1>",
  "imagem2": "<base64 da imagem 2>"
}
```

**Resposta:**

```json
{
  "resultado": true,
  "distancia": 0.3456
}
```

- `resultado`: `true` se os rostos são semelhantes, `false` caso contrário.
- `distancia`: valor numérico da distância de similaridade (quanto menor, mais semelhantes).

## Observações

- O modelo utilizado é o "ArcFace" do DeepFace.
- O parâmetro `enforce_detection=False` permite comparar imagens mesmo que não seja detectado um rosto perfeitamente.
- As imagens recebidas são removidas após o processamento.

## Contribuição

Pull requests são bem-vindos! Para grandes mudanças, abra uma issue primeiro para discutir o que você gostaria de modificar.

## Licença

Este projeto está sob a licença MIT.
