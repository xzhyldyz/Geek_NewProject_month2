class Animal:
    def speak(self):
        print("Animal speaking")


class Cat(Animal):
    def speak(self):
        print("мяу")
        super().speak()

class Dog(Animal):
    def speak(self):
        print("гав")
        super().speak()

class CatDog(Dog, Cat):
    def speak(self):
        print("гав мяу")
        super().speak()


kotopes = CatDog()
kotopes.speak()
print(CatDog.__mro__) # methods resolution order
print(Dog.__mro__)