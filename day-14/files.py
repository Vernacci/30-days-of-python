# working with files

with open('example.txt', 'a') as write_file:
    write_file.write('\nHello from the context manager')

with open('iris.csv', 'r') as iris_file:
    iris_data = iris_file.readlines()
    # print(iris_data)

ireses = []

for row in iris_data[1:]:
    sepal_length, sepal_width, petal_length, petal_width, species = row.strip().split(',')

    iris_dict = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
        "species": species
    }
    ireses.append(iris_dict)

# print(ireses)

# exercicios

# with open('hello.txt', 'a') as hello_file:
#     hello_text = hello_file.read()
#     hello_file.write('How are you?')

with open('new_iris.csv', 'a') as new_iris_file:
    new_iris = new_iris_file.write(str(ireses))
