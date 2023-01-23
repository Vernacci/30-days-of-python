# maps, filters, conditional comprehensions
from operator import add, methodcaller


def cube(number: list):
    return number ** 3


numbers = [1, 2, 3, 4, 5, 6]

cubed = map(cube, numbers)
print(cubed)

print(*cubed, sep=", ")


odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]

total = map(add, odds, evens)
print(*total, sep=', ')


names = ['ellie', 'joel', 'tess', 'tommy']

title_names = map(methodcaller("title"), names)
print(*title_names)


numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = [number for number in numbers if number % 2 == 0]


def is_even(number):
    return number % 2 == 0


numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = filter(is_even, numbers)
