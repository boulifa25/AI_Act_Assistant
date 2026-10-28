FROM python:3.11-slim

WORKDIR /app
ENV PYTHONUNBUFFERED=1 \
    HF_HOME=/opt/hf

# PyTorch CPU : l'image CUDA par défaut pèserait plusieurs Go de plus pour rien (seuls les embeddings tournent ici).
RUN pip install --no-cache-dir torch==2.14.1 --index-url https://download.pytorch.org/whl/cpu
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Modèle d'embeddings téléchargé au build : le conteneur démarre sans accès à Hugging Face.
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('intfloat/multilingual-e5-small')"

COPY app ./app

EXPOSE 8000
CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
