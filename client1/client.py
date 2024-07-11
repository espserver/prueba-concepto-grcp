import grpc
import greeter_pb2
import greeter_pb2_grpc
import time

def run():
    while True:
        try:
            with grpc.insecure_channel('server:50051') as channel:
                stub = greeter_pb2_grpc.GreeterStub(channel)
                while True:
                    response = stub.SayHello(greeter_pb2.HelloRequest(name='Cliente #1'))
                    print("Greeter client received: " + response.message)
                    time.sleep(5)
        except grpc.RpcError as e:
            print(f"Connection failed: {e}. Retrying...")
            time.sleep(5)

if __name__ == '__main__':
    run()
