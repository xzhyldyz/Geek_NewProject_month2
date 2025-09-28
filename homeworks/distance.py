class Distance:
    def __init__(self, value, unit="m"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.convert()} m"

    def __add__(self, other):
        return Distance(self.convert() + other.convert(), "m")

    def __sub__(self, other):
        result = self.convert() - other.convert()
        if result < 0:
            return f"Результат не может быть отрицательным"
        else:
            return Distance(result, "m")


    def convert(self):
        if self.unit == "m":
            return self.value
        elif self.unit == "cm":
            return self.value * 0.01
        elif self.unit == "km":
            return self.value * 1000
        else:
            return f"Неизвестная единица измерения"

