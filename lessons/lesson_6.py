class User:
    #переменные класса
    total_users = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.total_users += 1

    @classmethod
    def get_total_users(cls):
        return cls.total_users

    @classmethod
    def create_user(cls, name, email):
        if not  User.validate_email(email):
            # return None
            raise ValueError("Invalid email")
        user = cls(name, email)
        return user

    @staticmethod
    def validate_email(email):
        return "@" in email

print(User.get_total_users())

print(User.total_users)

user_1 = User("Albert", "albert@gmail.com")
user_2 = User("Igor", "igor@gmail.com")

user_1.total_users = 4

print(User.total_users)
print(user_1.total_users)

user_3 = User.create_user(name="John", email="johngmail.com")
print(user_3)