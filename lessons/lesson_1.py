class Car:
    # инициализатор
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive_to_location(self, location):
        print(f"Car {self.model} is drinig to {location}")

car_honda = Car("silver", "Honda")
print(car_honda)

car_subaru = Car("black", "Subaru")
print(car_subaru)
car_subaru.drive_to_location("Bishkek")
print(f"Car color {car_subaru.color}, model {car_subaru.model}")

car_honda.color = "red"
print(f"Car  color {car_honda.color}, model {car_honda.model}")

print(type(car_honda))
print(type(123123))
print(type("hello world"))

