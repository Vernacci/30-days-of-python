# imports
from fractions import Fraction
from math import fsum
from random import randint as rand

fraction = Fraction(12, 2)
print(fraction)

numbers = [1.43, 1.1, 5.32, 87.032, 0.2, 23.4]
print(fsum(numbers))

print(rand(1, 100))
