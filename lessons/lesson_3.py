class Car:
    # инициализатор
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.__fined = False
        self.__max_speed = 100

    def drive_to_location(self, location):
        print(f"Car {self.model} is driving to {location}, it is fined: {self.__fined}")

    def __test_car(self):
        print(f"test car {self.model}")

    def get_fined(self):
        # getter
        return self.__fined

    def get_max_speed(self):
        return self.__max_speed

    def set_fined(self, fined):
        # setter
        self.__fined = fined

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, max_speed):
        self.__max_speed = max_speed

class Bus(Car):
    def test_bus(self):
        print(f"test bus {self.get_fined()}")


car_honda = Car("black", "Honda Civic")
# print(car_honda._fined)
# car_honda._test_car()
# print(car_honda.__fined)
# car_honda.__test_car()
print(car_honda._Car__fined)
bus_40 = Bus("yellow", "Mercedes Benz")
bus_40.test_bus()
bus_40.set_fined(True)
print(bus_40.get_fined())
print(bus_40.max_speed)
bus_40.max_speed = 120
print(bus_40.max_speed)