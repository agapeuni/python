class Singleton:

    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print(" __init__ method called..")
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s1 = Singleton()  # class initialized, but object not created
print("1 Object created", s1)
print("2 Object created", Singleton.getInstance())  # Gets created here
s2 = Singleton()  # instance already created
print("3 Object created", s2)