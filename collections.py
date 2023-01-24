# basic python collections

# lists
names = ["Victor", "Frezin", "Yanal"]

# movies = [
#     "O brilho eterno de uma mente sem lembranças",
#     "Batman o Cavaleiro das Trevas",
#     "V de Vingança",
# ]

names.append("Emanuweb")
names.remove("Victor")
names.insert(2, "Mirongas")
del names[1]
names.pop()
print(names)

# tuples are immutable
colleagues = ("Jesse", "Walter", "Mike", "Gus")

# exercício
movies = [("Psicopata Americano", 2000, 7000000)]

movie_title = input("Type the movie name: ")
movie_release_year = input("type the movie release year: ")
movie_budget = input("type the movie budget: ")

new_movie = movie_title, movie_release_year, movie_budget
movies.append(new_movie)
print(movies)
