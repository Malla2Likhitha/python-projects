def add(*args):   # can be named anything.... *numbers
    arg_sum = 0
    # print(args[1])
    for arg in args:
        arg_sum += arg
    return arg_sum


print(add(2, 3, 2, 1, 4, 5, 6, 1, 1))
# args are being passed as a tuple


def calculate(n, **kwargs):
    # PEMDAS
    n *= kwargs['multiply']
    n /= kwargs['divide']
    n += kwargs['add']
    return n


print(calculate(2, add=3, multiply=5, divide=0.5))
# kwargs are being passed as a dictionary


class Car:

    def __init__(self, **kw):
        print(kw)
        self.make = kw["make"]   # will get an error if make arg is not provided
        self.model = kw.get("model")   # will return None if model arg is not provided
        self.color = kw.get('color')


my_car = Car(make='Nissan', model='GT-R', color='Red')
print(my_car.model)
