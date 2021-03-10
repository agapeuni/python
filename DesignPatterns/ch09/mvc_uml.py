class Model(object):
    def logic(self):
        data = '샘플 데이터'
        print("Model: 비즈니스 로직별로 데이터 처리")
        return data


class View(object):
    def update(self, data):
        print("View: 데이터 업데이트:", data)


class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def interface(self):
        print("Controller: 클라이언트 요청을 전달")
        data = self.model.logic()
        self.view.update(data)


class Client(object):
    print("Client: 정보를 요청")
    controller = Controller()
    controller.interface()
