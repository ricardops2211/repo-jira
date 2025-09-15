FROM python:3.11-slim

# Instalar dependencias básicas
RUN apt-get update && \
    apt-get install -y ansible sshpass && \
    rm -rf /var/lib/apt/lists/*

# Crear directorio de la app
WORKDIR /app

# Copiar código de la app (desde la raíz del repo)
COPY app /app

# Instalar dependencias Python (si existe requirements.txt)
# RUN pip install -r requirements.txt

CMD ["python", "main.py"]
