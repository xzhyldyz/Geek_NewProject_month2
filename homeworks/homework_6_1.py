from datetime import datetime as dt

time_now = dt.now()
print(time_now.year)
print(time_now.month)
print(time_now.day)
print(time_now.hour)
print(time_now.minute)
print(time_now.second)

def checktime(func):
    def wrapper(*args, **kwargs):
        time_now = dt.now().strftime("%H:%M:%S %d/%m/%Y")
        print(f"Функция была вызвана в {time_now}")
        return func(*args, **kwargs)

    return wrapper

@checktime
def hello_world():
    print("hello world")

hello_world()