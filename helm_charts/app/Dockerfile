FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    curl \
    nano \
    iputils-ping \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Instalar AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf awscliv2.zip aws

# Copiar archivos al contenedor
COPY . /app

# Instalar dependencias de Python
RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    pillow \
    boto3 \
    pytest \
    httpx \
    tensorflow-cpu \
    python-multipart

# Descargar pesos del modelo MobileNetV2
RUN python -c "from tensorflow.keras.applications import MobileNetV2; MobileNetV2(weights='imagenet')"

# Exponer el puerto
EXPOSE 8081

# Comando para ejecutar la app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]
