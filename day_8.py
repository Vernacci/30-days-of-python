# while loops
# user_input = int(input("Type a number: "))

# while user_input < 10:
#     print("Your number was less than 10")
#     user_input = int(input("Type another number: "))

# print("Your number was at least 10")

# while True:
#     selected_option = input("Digite A, B ou C, ou Q para sair")
#     if selected_option == "a":
#         print("voce escolheu A")
#     elif selected_option == "b":
#         print("voce escolheu B")
#     elif selected_option == "c":
#         print("voce escolheu C")
#     elif selected_option == "q":
#         break
#     else:
#         print("Argumento invalido")


for number in range(10):
    if number % 2 != 0:
        continue
    print(number)


# exercicios
lucky_number = 45


while True:
    user_number = int(input("Guess the number: "))
    if user_number < lucky_number:
        print("too low")
    elif user_number > lucky_number:
        print("too high")
    elif user_number == lucky_number:
        print("you got it")
        break

for n in "Python":
    if n == "o":
        continue
    print(n)
