# Construire l'image

docker build -t flask-server .

# Executer l'image

# (http://localhost:8080/ pour y acceder)

docker run -d -p 8080:80 flask-server

# (le -d n'est pas obligatoire il est plus facile d'arreter le container si il n'est pas dasn la commande)
