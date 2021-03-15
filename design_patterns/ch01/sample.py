class Car(object):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_car(self,):
        return "<Car (%s, %s)>" % (self.name, self.price)


p = Car("SM6", 3200)
print("type = ", type(p))
print("id = ", id(p))
print(p.show_car())
