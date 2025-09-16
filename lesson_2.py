class Car:
    # инициализатор
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive_to_location(self, location):
        print(f"Car {self.model} is driving to {location}")

class Bus(Car):
    def __init__(self, color, model, number):
        super().__init__(color, model)
        self.number = number

    def drive_to_location(self, location):
        print(f"Bus {self.model} is driving to {location}")

    def test_bus(self):
        print(f"Bus test {self.color}")

bus1 = Bus("red", "Honday", "123")
bus1.drive_to_location("Bishkek")
print(bus1.color)

