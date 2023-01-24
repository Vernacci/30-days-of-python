# functions
def get_even_numbers(amount: int):
    for number in range(1, amount + 1):
        print(number * 2)


# get_even_numbers(30)


def x_print(output, amount):
    for _ in range(amount + 1):
        print(output)


# x_print('Fortnaite ou la babadi???', 12)

# exercicios

def add(x: int, y: int):
    print(x + y)


def subtract(x: int, y: int):
    print(x - y)


def multiply(x: int, y: int):
    print(x * y)


def divide(x: int, y: int) -> float:
    print(x / y)


add(1, 1)
subtract(2, 2)
multiply(2, 2)
divide(4, 4)


def print_show(show: dict):
    print(
        f'{show["title"]} has {show["seasons"]} seasons and was released in {show["initial_release"]}')


series = [
    {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
    {"title": "Fargo", "seasons": 4, "initial_release": 2014},
    {"title": "Firefly", "seasons": 1, "initial_release": 2002},
    {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
    {"title": "True Detective", "seasons": 3, "initial_release": 2014},
    {"title": "Westworld", "seasons": 3, "initial_release": 2016},
]

for i in series:
    print_show(i)
