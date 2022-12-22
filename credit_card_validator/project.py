# credit card validator project

user_card_number = list(input('type your credit card number: ').strip())

check_digit = user_card_number.pop()
user_card_number.reverse()

processed_digits = []

for index, digit in enumerate(user_card_number):
    if index % 2 == 0:
        doubled_digit = int(digit) * 2
        if doubled_digit > 9:
            doubled_digit -= 9
        processed_digits.append(doubled_digit)
    else:
        processed_digits.append(int(digit))

if sum(processed_digits) % 10 == 0:
    print('Valid card number!')
else:
    print('Invalid Card number, try again!')
