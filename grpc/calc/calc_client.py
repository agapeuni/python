
import grpc

import calc_pb2
import calc_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50050')
    stub = calc_pb2_grpc.CalculatorStub(channel)

    response = stub.Add(calc_pb2.AddRequest(n1=20, n2=10))
    print("+", response.n1)
    
    response = stub.Substract(calc_pb2.SubstractRequest(n1=20, n2=10))
    print("-", response.n1)

    response = stub.Multiply(calc_pb2.MultiplyRequest(n1=20, n2=10))
    print("*", response.n1)

    response = stub.Divide(calc_pb2.DivideRequest(n1=20, n2=10))
    print("/", response.f1)


if __name__ == '__main__':
    run()
