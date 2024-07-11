FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .
RUN pip install grpcio google-api-python-client
CMD ["python", "client.py"]
