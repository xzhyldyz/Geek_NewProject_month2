class Money:
    def __init__(self, amount=0):
        self.amount = amount

    def __str__(self):
        return f"экземпляр Money: {self.amount}"

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __sub__(self, other):
        pass

igor_money = Money(100)
print(igor_money)
adilet_money = Money(250)
total_money = igor_money + adilet_money
print(total_money)