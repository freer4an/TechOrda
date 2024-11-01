curl -LJO https://stepik.org/media/attachments/lesson/686238/jusan-dockerfile.conf
curl -LJO https://stepik.org/media/attachments/lesson/686238/jusan-dockerfile.zip
unzip jusan-dockerfile.zip -d .

cat << EOF > Dockerfile 
FROM nginx:mainline
COPY jusan-dockerfile.conf /etc/nginx/conf.d/jusan-dockerfile.conf
COPY jusan-dockerfile /var/www/jusan-dockerfile
RUN rm /etc/nginx/conf.d/default.conf
EOF

docker build -t nginx:jusan-dockerfile .
docker run --name jusan-dockerfile -d -p 6060:80 nginx:jusan-dockerfile