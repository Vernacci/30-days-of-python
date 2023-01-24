# *args (can have any name)
def greet(*name):
    for n in name:
        print(f'Hello {n}')


greet('vito', 'emanuel', 'bosta', 'frezin', 'mirongas')

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(*numbers, sep=' | ')


# keyword arguments

def print_movie(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}, {value}')


movie = {
    "title": "O brilho eterno de uma mente sem lembranças",
    "director": "alguem ai",
    "release": "2000"
}

print_movie(**movie)


# exercicios

def sum_args(*args):
    return sum(args)


print(sum_args(2, 2, 2, 2, 2))


def args_kwargs(*args, **kwargs):
    for x in args:
        print(f'{x} is a positional argument')

    for key, value in kwargs.items():
        print(f'{key}: {value} | is a keyword argument')


args_kwargs("ronaldo", sexo="babadi")

country = {
    "name": "Germany",
    "population": "83 million",
    "capital": "Berlin",
    "currency": "Euro"
}


def print_country(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


print_country(**country)
