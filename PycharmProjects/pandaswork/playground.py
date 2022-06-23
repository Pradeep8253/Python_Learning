def add(*args):
    # print(args[2])
    sum = 0
    for n in args:
        sum += n
    return sum


# print(add(3, 5, 6, 8))


def calculate(n, **kwargs):
    # print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]

    # print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Tata", model="Truck" , color="red", seats="155")
print(my_car.make)
print(my_car.model)
print(my_car.color)
print(my_car.seats)
