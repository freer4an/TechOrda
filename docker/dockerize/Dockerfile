FROM python:latest
WORKDIR /app
RUN apt update && apt install uvicorn
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py .
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]