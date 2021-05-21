import grpc

import demo_pb2
import demo_pb2_grpc

try:
    # Creates an insecure Channel to a server.
    channel = grpc.insecure_channel('localhost:50051')
    stub = demo_pb2_grpc.DemoStub(channel)

    demoRequest = demo_pb2.DemoRequest(name='kor', count=10)
    demoResponse = stub.Select(demoRequest)
    print(demoResponse.name, demoResponse.total)

    demoRequest = demo_pb2.DemoRequest(name='jpn', count=11)
    demoResponse = stub.Select(demoRequest)
    print(demoResponse.name, demoResponse.total)

    demoRequest = demo_pb2.DemoRequest(name='eng', count=12)
    demoResponse = stub.Select(demoRequest)
    print(demoResponse.name, demoResponse.total)
except Exception as e:
    print(e)
