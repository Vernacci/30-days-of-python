# string concatanation/interpolation (f strings)
# pode ser feito também utilizando o sinal + para juntar strings
# ou então usando o .format()


# exercício
greeting = "Hello, world"
print(f"{greeting}!")

user_name = input("Type your name: ")
print(f"Hello {user_name}, how are you?")


title = "Joker"
director = "Todd Phillips"
release_year = str(2019)

print(f"{title}({release_year}), directed by {director}")
