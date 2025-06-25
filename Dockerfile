# Utiliser une image Python légère
FROM python:3.10-slim

# Définir le dossier de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
COPY app.py .
COPY mlruns/ ./mlruns/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port
EXPOSE 5000

# Commande de démarrage
CMD ["python", "app.py"]
