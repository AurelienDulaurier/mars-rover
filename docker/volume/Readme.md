docker build -t volume_image .

docker run -v "$(pwd)/index.html:/usr/share/nginx/html/index.html" -p 8080:80 volume_image
