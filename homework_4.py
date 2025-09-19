class Vehicle:
    def start(self):
        print("Vehicle starting")

class Car(Vehicle):
    def start(self):
        print("Car starting")
        super().start()

class ElectricCar(Vehicle):
    pass


class Tesla(ElectricCar, Car):
    def start(self):
        print("Tesla ready")
        super().start()

Tesla().start()
