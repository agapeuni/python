from abc import ABCMeta, abstractmethod


class AbstractClass(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    def template_method(self):
        print("알고리즘 정의.")
        self.operation2()
        self.operation1()


class ConcreteClass(AbstractClass):

    def operation1(self):
        print("작업1")

    def operation2(self):
        print("작업2")


class Client:
    def main(self):
        self.concreate = ConcreteClass()
        self.concreate.template_method()


client = Client()
client.main()
