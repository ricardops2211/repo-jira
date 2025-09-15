FROM python:3.11-slim

# Instalar dependencias básicas
RUN apt-get update && \
    apt-get install -y ansible sshpass && \
    rm -rf /var/lib/apt/lists/*

# Directorio de la app
WORKDIR /app

# Copiar código de la app (carpeta app del repo)
COPY app/ /app/

# Instalar dependencias si existen
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Comando por defecto
CMD ["python", "main.py"]
