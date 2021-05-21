import grpc

import part_pb2
import part_pb2_grpc


def showPart(partResponse):
    print("We have {2} [{0}] {1}.".format(
        partResponse.id, partResponse.name, partResponse.total))


def run():
    try:
        # Creates an insecure Channel to a server.
        channel = grpc.insecure_channel('localhost:50052')
        stub = part_pb2_grpc.PartStub(channel)

        # getPartList
        print("")
        print("@@ getPartList call")
        partRequest = part_pb2.PartRequest()
        partResponse = stub.getPartList(partRequest)
        print("@@ part_list =", partResponse.part_list)

        # getPart
        print("")
        print("@@ getPart call")
        partRequest = part_pb2.PartRequest(id='ID01', count=10)
        partResponse = stub.getPart(partRequest)
        if partResponse.result:
            showPart(partResponse)
        else:
            print('Failed! getPart [{0}]'.format(partResponse.id))

        # getPart
        print("")
        print("@@ getPart")
        partRequest = part_pb2.PartRequest(id='ID02', count=20)
        partResponse = stub.getPart(partRequest)
        if partResponse.result:
            showPart(partResponse)
        else:
            print('Failed! getPart [{0}]'.format(partResponse.id))

        # getPart
        print("")
        print("@@ getPart")
        partRequest = part_pb2.PartRequest(id='ID03', count=30)
        partResponse = stub.getPart(partRequest)
        if partResponse.result:
            showPart(partResponse)
        else:
            print('Failed! getPart [{0}]'.format(partResponse.id))

        # getPart
        print("")
        print("@@ getPart call")
        partRequest = part_pb2.PartRequest(id='ID04', count=40)
        partResponse = stub.getPart(partRequest)
        if partResponse.result:
            showPart(partResponse)
        else:
            print('Failed! getPart [{0}]'.format(partResponse.id))

        # createPart
        print("")
        print("@@ createPart call")
        partRequest = part_pb2.PartRequest(
            id='ID05', name='Dry Cell', count=10)
        partResponse = stub.createPart(partRequest)
        if partResponse.result:
            print("[{0}] {1} have been added successfully.".format(
                partResponse.id, partResponse.name))
        else:
            print("[{0}] {1} already exists.".format(
                partResponse.id, partResponse.name))

        # modifyPart
        print("")
        print("@@ modifyPart call")
        partRequest = part_pb2.PartRequest(
            id='ID01', name='Adaptor', count=100)
        partResponse = stub.modifyPart(partRequest)
        if partResponse.result:
            print("[{0}] {1} has been changed to {2}".format(
                partResponse.id, partResponse.name, partResponse.total))
        else:
            print("[{0}] does not exist.".format(partResponse.id))

        # changePart
        print("")
        print("@@ changePart call")
        partRequest = part_pb2.PartRequest(
            id='ID04', name='Power Motor', count=300, change_name='ID06')
        partResponse = stub.changePart(partRequest)
        if partResponse.result:
            print("[{0}] has been changed to [{1}] {2}, {3}".format(
                partResponse.id, partResponse.change_name, partResponse.name, partResponse.total))
        else:
            print("[{0}] does not exist.".format(partResponse.id))

        # getPart
        print("")
        print("@@ getPart call")
        partRequest = part_pb2.PartRequest(id='ID06', count=50)
        partResponse = stub.getPart(partRequest)
        if partResponse.result:
            showPart(partResponse)
        else:
            print('Failed! getPart [{0}]'.format(partResponse.id))

        # removePart
        print("")
        print("@@ removePart call")
        partRequest = part_pb2.PartRequest(id='ID05')
        partResponse = stub.removePart(partRequest)
        if partResponse.result:
            print("[{0}] has been deleted.".format(partResponse.id))
        else:
            print("[{0}] does not exist.".format(partResponse.id))

        # getPartList
        print("")
        print("@@ getPartList call")
        partRequest = part_pb2.PartRequest()
        partResponse = stub.getPartList(partRequest)
        print("@@ part_list =", partResponse.part_list)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    run()