class Person:
    def __init__(self, name, birth_date, occupation, higher_education = "You dont have"):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f"Hello {self.name},\nYour birth date is: {self.birth_date},\nYour occupation {self.occupation}\nYour higher education is: {self.higher_education}")


naruto = Person("Naruto", "10.10.2000", "Hokage")
naruto.introduce()

itachi = Person("Itachi", "June 9th", "a terrorist from the Akatsuki", "Yes I have")
itachi.introduce()

hinata = Person("Hinata", "December 27th", "Heiress to the Hyūga Clan", "Yes I have")
hinata.introduce()