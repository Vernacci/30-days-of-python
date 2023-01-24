# split join and slices

project_authors = ["Mike", "Jesse", "Walter"]

project_authors = ", ".join(project_authors)
print(f"As pessoas que trabalharam neste projeto foram: {project_authors}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

str_numbers = []


for n in numbers:
    str_numbers.append(str(n))

print(", ".join(str_numbers))

print("------------------------------")

# user_numbers = input("digite uma sequencia de numeros separados por virgula: ")
# list_numbers = user_numbers.split(",")

# print(list_numbers)
# print("----------------------------------")

# slice
string = "python"
sliced_string = string[0:3]  # pyt
sliced_string = string[3:]  # hon
print(sliced_string)
print("---------------------------")

# exercicios

# user_name = input("digite seu nome e sobrenome: ")
# name_collection = user_name.split()
# print(name_collection)

# name = name_collection[0]
# surname = name_collection[1]

# print(f"{name}, {surname}")


nums = [1, 2, 3, 4, 5]
str_nums = []

for n in nums:
    str_nums.append(str(n))

print(" | ".join(str_nums))

quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'",
]

for q in quotes:
    print(q[1:-2])

user_input = input("Digite algo para extrair a quantidade de caracteres: ")

user_input.strip()
print(len(user_input))
