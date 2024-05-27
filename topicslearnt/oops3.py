# Abstraction
class Car:
    def __init(self, acc, brk, clutch):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started!")


car1 = Car()
car1.start()
