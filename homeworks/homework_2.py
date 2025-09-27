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
    def __init__(self,name, birth_date, occupation, village, higher_education="You dont have"):
        super().__init__(name, birth_date, occupation, higher_education)
        self.village = village

    def introduce(self):
        print(f"Привет {self.name}! Довольно интересная у тебя должность: {self.occupation} в {self.village}.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, skills, higher_education="You dont have"):
        super().__init__(name, birth_date, occupation, higher_education)
        self.skills = skills

    def introduce(self):
        print(f"Как ты {self.name}? Кстати, у меня тоже день рождения в {self.birth_date} как и у тебя! И да твои способности {self.skills} восхитительны!")


shikamaru = Classmate("Shikamaru", "September 22", "Shinobi", "Деревне скрытого листа")
shikamaru.introduce()
gaara = Classmate("Gaara", "January 19", "Hokage", "Деревня скрытого в песке")
gaara.introduce()

kakashi = Friend("Kakashi", "September 15", "Shinobi", "Mangekyō Sharingan")
kakashi.introduce()
obito = Friend("Obito", "February 10", "Shinobi", "Mangekyō Sharingan")
obito.introduce()


for prsn in[shikamaru, gaara, kakashi, obito]:
    prsn.introduce()
