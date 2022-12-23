# sets
vegetables = {'carrot', 'lettuce', 'brocolli', 'onion'}
vegetables.add('potato')
vegetables.update(['pumpkin', 'idk'])
vegetables.remove('carrot')


letters = {'a', 'b', 'c'}
numbers = {1, 2, 3}

letters_and_numbers = letters.union(numbers)
# print(letters_and_numbers)

mod_2 = {2, 4, 6, 8, 10, 12, 14, 16, 18}
mod_3 = {3, 6, 9, 12, 15, 18}

mod_6 = mod_2.intersection(mod_3)
# print(mod_6)

bundle_1 = {'Fortnite', 'Rocket League', 'Counter Strike'}
bundle_2 = {'Fortnite', 'Overwatch', 'Sekiro'}

# print(bundle_2.difference(bundle_1))
# print(bundle_1.symmetric_difference(bundle_2))

# exercicios
set_1 = set()

set_1.update(['Victor', 'Frezin', 'Emanuweb', 'Yanal', 'Mirongas'])
print(set_1)

set_2 = {'Victor', 'An'}

print(set_1.difference(set_2))
print(set_1.intersection(set_2))
print(set_1.symmetric_difference(set_2))


nums = range(10)

user_input = int(input('Type your number: '))

if user_input in nums:
    print('Your number was in range')
else:
    print('Your number was out of the range')
