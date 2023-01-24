# first class functions / lambda

def add(a, b):
    return a + b


adder = add

del add


print(adder(1, 1))
print(adder)

students = [
    {"name": "Hannah", "grade_average": 100},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]


def get_average_grade(student):
    return student["grade_average"]


def get_student_name(student):
    return student["name"]


highest_grade = max(students, key=lambda student: student["grade_average"])
# print(highest_grade)

print(students.sort(key=get_student_name))


# def add(a, b):
#     print(a + b)


# def subtract(a, b):
#     print(a - b)


# def multiply(a, b):
#     print(a * b)


# def divide(a, b):
#     if b == 0:
#         print("You can't divide by 0!")
#     else:
#         print(a / b)


# operations = {
#     "a": add,
#     "s": subtract,
#     "m": multiply,
#     "d": divide
# }

# selected_options = input("""Please select one of the options:
# a: add
# s: subtract
# m: multiply
# d: divide

# """)

# operation = operations.get(selected_options)

# if operation:
#     a = int(input('Enter a value for A: '))
#     b = int(input('Enter a value for B: '))
#     operation(a, b)
# else:
#     print('not a valid operation')

def exp(base, exponent): return base ** exponent


print(exp(2, 2))
