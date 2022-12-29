# working with files

with open('example.txt', 'a') as write_file:
    write_file.write('\nHello from the context manager')

with open('iris.csv', 'r') as iris_file:
    iris_data = iris_file.readlines()
    print(iris_data)
