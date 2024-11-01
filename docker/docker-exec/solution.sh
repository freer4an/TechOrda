docker run --name jusan-docker-exec -d -p 8181:80 nginx:mainline 
docker exec -it jusan-docker-exec bash
cat << EOF > /etc/nginx/conf.d/jusan-docker-exec.conf
server {
    listen 80;
    server_name jusan.singularity;

    location / {return 200 'Hello, from jusan-docker-exec';}
    location /home {return 201 'This is my home!';}
    location /about {return 202 'I am just an exercise!';}
}
EOF
rm /etc/nginx/conf.d/default.conf
nginx -s reload
exit