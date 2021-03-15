class Borg:
    __shared_state = {"1":"2"}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass

b1 = Borg()
b2 = Borg()
b1.x = 4

print("Borg Object 'b1': ", b1)
print("Borg Object 'b2': ", b2)

print("Object State 'b1':", b1.__dict__)
print("Object State 'b2':", b2.__dict__)