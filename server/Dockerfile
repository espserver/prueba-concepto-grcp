FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .
RUN pip install grpcio grpcio-tools google-api-python-client
# RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. greeter.proto
CMD ["python", "server.py"]
