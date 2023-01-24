# conditionals and booleans

print(bool(5 > 10))
print(bool(1 < 10))
print("A" < "a")

print("---------------------------------")
a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))

print(a == b)
print(a is b)

print("---------------------------------")

# conditionals

# age = int(input("type your age: "))

# if age < 18:
#     print("we cant serve you")
# else:
#     print("have a nice stay")


# exercicios

numbers = [1, 2, 3, 4]

new_numbers = numbers + [5]

numbers.append(5)
numbers.append(10)

print(id(numbers))

print(id(new_numbers))

print(numbers == new_numbers)

print(numbers is new_numbers)

print("---------------------------------")


user_num = int(input("type a number: "))

if user_num == 0:
    print("your number is zero")
elif user_num < 0:
    print("your number is negative")
else:
    print(user_num)
