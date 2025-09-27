from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
   def make_sound(self):
       print("gav gav")


class Cat(Animal):
    def make_sound(self):
        print("miau miau")


puppy = Dog()
puppy.make_sound()