#créer réseau
docker network create my_network

#créer deux conteneurs et les associer au réseau
docker run -d --name container1 --network mon_reseau alpine
docker run -d --name container2 --network mon_reseau alpine

#lancer le shell du'un container
docker exec -it container1 /bin/sh

#ping le deuxieme
docker exec -it container1 /bin/sh