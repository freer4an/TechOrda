cat << EOF > Dockerfile
FROM python:latest
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py .
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
EOF
docker build -t jusan-fastapi-final:dockerized .
docker run --name jusan-dockerize -d -p 8080:8080 jusan-fastapi-final:dockerized