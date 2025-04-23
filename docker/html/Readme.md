# Construire l'image

docker build -t static-website .

# Executer l'image

# (http://localhost:81/ pour y acceder)

docker run -d -p 81:80 static-website
