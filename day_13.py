# scope and returning values from functions

def greet(name):
    greeting = f'Hello, {name}'
    print(greeting)

# print(greeting) = error


# namespaces / globals
names = ['Victor', 'Fabricio', 'Emanuweb']
x = 1234


def add(a, b):
    print(locals())
    print(a, b)


add(1, 3)
print('----------------------')
print(globals())

# return


def divide(a, b):
    return a / b


value = divide(2, 2)
print(value)

print(divide(4, 2))
