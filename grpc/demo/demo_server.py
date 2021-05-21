from concurrent import futures
import logging

import grpc

import demo_pb2
import demo_pb2_grpc


class Demo(demo_pb2_grpc.DemoServicer):

    def Select(self, request, context):
        print(request.name, request.count)
        total = 100
        
        if request.name == 'kor':
            fullname = "Korea"
            total = total + request.count
        elif request.name == 'eng':
            fullname = "English"
            total = total + request.count
        elif request.name == 'jpn':
            fullname = "Japan"
            total = total + request.count
        return demo_pb2.DemoResponse(name=fullname, total=total)


def serve():
    # Creates a Server with which RPCs can be serviced.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    demo_pb2_grpc.add_DemoServicer_to_server(Demo(), server)

    # Opens an insecure port for accepting RPCs.
    server.add_insecure_port('[::]:50051')

    # Starts this Server.
    server.start()

    # Block current thread until the server stops.
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
