# exception handling
import math

# while True:
#     try:
#         number = int(input('enter your age: '))
#         break
#     except ValueError:
#         print('You need to enter an integer!')


def average(numbers: list) -> float:
    try:
        mean = math.fsum(numbers) / len(numbers)
        print(mean)
    except (ZeroDivisionError, TypeError):
        print('Cannot calculate the average with the numbers you provided')


average([10, 6.5, 8, 4])
average(0)
