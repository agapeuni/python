from concurrent import futures
import logging

import grpc

import part_pb2
import part_pb2_grpc


class Part(part_pb2_grpc.PartServicer):

	partInfo = {
		'ID01': ['Antenna', 0],
		'ID02': ['Battery', 0],
		'ID03': ['Charger', 0],
		'ID04': ['Motor', 0]
	}

	def getPartList(self, request, context):
		print("@@ getPartList =", request)

		part_list = ''
		result = False

		if len(self.partInfo) > 0:
			part_list = self.partInfo
			result = True
		else:
			part_list = 'None'

		print('Result:', result, '\\', self.partInfo)
		return part_pb2.PartResponse(part_list=str(part_list), result=result)

	def getPart(self, request, context):
		print("@@ getPart =", request)

		id = request.id
		name = ''
		count = request.count
		total = 0
		result = False

		# Check Required Value
		if id is None or count is None:
			return part_pb2.PartResponse(result=result)

		if id in self.partInfo:
			name = self.partInfo[id][0]
			total = self.partInfo[id][1] + count
			self.partInfo[id][1] = total
			result = True
		else:
			name = 'None'
			total = 0

		print('Result:', result, '\\', self.partInfo)
		return part_pb2.PartResponse(id=id, name=name, total=total, result=result)

	def createPart(self, request, context):
		print("@@ createPart =", request)

		id = request.id
		name = request.name
		result = False

		# Check Required Value
		if id is None or name is None:
			return part_pb2.PartResponse(result=result)

		if id in self.partInfo:
			name = 'None'
		else:
			self.partInfo[id] = [name, 0]
			total = 0
			result = True

		print('Result:', result, '\\', self.partInfo)
		return part_pb2.PartResponse(id=id, name=name, total=total, result=result)
	def modifyPart(self, request, context):
		print("@@ modifyPart =", request)

		id = request.id
		name = request.name
		count = request.count
		result = False

		# Check Required Value
		if id is None:
			return part_pb2.PartResponse(result=result)

		if id in self.partInfo:
			self.partInfo[id] = [name, count]
			total = count
			result = True
		else:
			name = 'None'
			count = 0
			total = 0

		print('Result:', result, '\\', self.partInfo)
		return part_pb2.PartResponse(id=id, name=name, total=total, result=result)

	def changePart(self, request, context):
		print("@@ changePart =", request)

		id = request.id
		name = request.name
		change_name = request.change_name
		count = request.count
		result = False

		# Check Required Value
		if id is None or name is None or change_name is None or count is None:
			return part_pb2.PartResponse(result=result)

		if id in self.partInfo:
			del self.partInfo[id]
			self.partInfo[change_name] = [name, count]
			total = count
			result = True
		else:
			name = 'None'
			total = 0

		print('Result:', result, '\\', self.partInfo)
		return part_pb2.PartResponse(id=id, name=name, change_name=change_name, total=total, result=result)

	def removePart(self, request, context):
		print("@@ removePart =", request)

		id = request.id
		result = False

		# Check Required Value
		if id is None:
			return part_pb2.PartResponse(result=result)

		if id in self.partInfo:
			del self.partInfo[id]
			result = True
		else:
			pass

		print('Result:', result, '\\', self.partInfo)
		return part_pb2.PartResponse(id=id, result=result)


def serve():
	# Creates a Server with which RPCs can be serviced.
	print("gRPC Server Start...")
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	part_pb2_grpc.add_PartServicer_to_server(Part(), server)

	# Opens an insecure port for accepting RPCs.
	server.add_insecure_port('[::]:50052')

	# Starts this Server.
	server.start()

	# Block current thread until the server stops.
	server.wait_for_termination()


if __name__ == '__main__':
	logging.basicConfig()
	serve()