# list comprehensions
names = ['frezin', 'vito', 'emanuweb', 'yanal', 'mirongas']

names = [name.title() for name in names]
print(names)


# exercicios
numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]

print(squares)

movie = {
    "title": "thor: ragnarok",
    "director": "taika waititi",
    "producer": "kevin feige",
    "production_company": "marvel studios"
}

updated_movie = {key: value.title() for key, value in movie.items()}
print(updated_movie)
