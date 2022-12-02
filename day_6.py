# for loops

movies = [
    ("Eternal Sunshine of the Spotless Mind", "Michel Gondry", 2004),
    ("Memento", "Christopher Nolan", 2000),
    ("Requiem for a Dream", "Darren Aronofsky", 2000),
]

for movie in movies:
    if movie[0] == "Memento":
        print("esse filme ja foi visto")
        break

print(range(3, 10))
