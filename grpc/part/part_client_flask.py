from flask import Flask
from flask import jsonify

import grpc

import part_pb2
import part_pb2_grpc


app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    app.logger.debug('404 error')
    return '404 error'


@app.route('/partlist', methods=['GET'])
def partlist():
    try:
        # Creates an insecure Channel to a server.
        channel = grpc.insecure_channel('localhost:50052')
        stub = part_pb2_grpc.PartStub(channel)

        # getPartList call
        partRequest = part_pb2.PartRequest()
        partResponse = stub.getPartList(partRequest)
        if partResponse.result:
            return jsonify(partResponse.part_list)
        else:
            app.logger.debug('Failed! getPart [{0}]'.format(partResponse.id))

    except Exception as e:
        print(e)


@app.route('/part/<id>', methods=['GET'])
def getPart(id):
    try:
        # Creates an insecure Channel to a server.
        channel = grpc.insecure_channel('localhost:50052')
        stub = part_pb2_grpc.PartStub(channel)

        # getPart call
        partRequest = part_pb2.PartRequest(id=id, count=0)
        partResponse = stub.getPart(partRequest)
        if partResponse.result:
            print(partResponse)
            return jsonify({
                "id": partResponse.id,
                "name": partResponse.name,
                "total": partResponse.total
            })
        else:
            app.logger.debug('Failed! getPart [{0}]'.format(partResponse.id))

    except Exception as e:
        print(e)


@app.route('/part/<id>/<int:count>', methods=['GET'])
def getPartWithCount(id):
    try:
        # Creates an insecure Channel to a server.
        channel = grpc.insecure_channel('localhost:50052')
        stub = part_pb2_grpc.PartStub(channel)

        # getPart call
        partRequest = part_pb2.PartRequest(id=id, count=10)
        partResponse = stub.getPart(partRequest)
        if partResponse.result:
            print(partResponse)
            return jsonify({
                "id": partResponse.id,
                "name": partResponse.name,
                "total": partResponse.total
            })
        else:
            print('Failed!')

    except Exception as e:
        print(e)


if __name__ == '__main__':
    print("Web Server Start...")
    app.run(debug=True)
