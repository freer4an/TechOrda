curl -LJO https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.conf
curl -LJO https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.zip
unzip jusan-docker-mount.zip -d .
docker run -d --name jusan-docker-mount -p 9999:80 \
    --mount type=bind,source="$(pwd)"/jusan-docker-mount.conf,target=/etc/nginx/conf.d/jusan-docker-mount.conf \
    --mount type=bind,source="$(pwd)"/jusan-docker-mount,target=/var/www/example \
    nginx:mainline
docker exec jusan-docker-mount rm /etc/nginx/conf.d/default.conf
docker exec jusan-docker-mount nginx -s reload
