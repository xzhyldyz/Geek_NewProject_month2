def printer(func):
    def wrapper(*args, **kwargs):
        print(f"До вызова фун-ии {func.__name__}")
        result = func(*args, **kwargs)
        print(f"После вызова фун-ии {func.__name__}")
        return result

    return wrapper

@printer
def hello_world():
    print("hello world")

@printer
def add_numbers(number1, number2):
    return number1 + number2

hello_world()
print(add_numbers(2, 3))

def blahblah():
    print("blah blah")

blahblah = printer(blahblah)
blahblah()

