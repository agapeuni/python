class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

FourCal.setdata(a, 4, 2)

a = FourCal()
a.setdata(4, 2)

print(a.add())
