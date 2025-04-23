# Utiliser l'image de base Python
FROM python:3.9-slim

# Répertoire travail
WORKDIR /app

# Copier le fichier de requirements (dans le fichier défini au dessus)
COPY requirements.txt requirements.txt

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY app.py app.py

EXPOSE 5000

CMD ["python", "app.py"]