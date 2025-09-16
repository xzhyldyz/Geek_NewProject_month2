class Person:
    def __init__(self, name, birth_date, occupation, higher_education="You dont have"):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(
            f"Hello {self.name},\nYour birth date is: {self.birth_date},\nYour occupation {self.occupation}\nYour higher education is: {self.higher_education}")


class Classmate(Person):
    def introduce(self):
        print(f"Привет {self.name}! Довольно интересная у тебя должность: {self.occupation}.")


class Friend(Person):
    def introduce(self):
        print(f"Как ты {self.name}? Кстати, у меня тоже день рождения в {self.birth_date} как и у тебя!")


shikamaru = Classmate("Shikamaru", "September 22", "Shinobi")
shikamaru.introduce()

kakashi = Friend("Kakashi", "September 15", "Shinobi")
kakashi.introduce()