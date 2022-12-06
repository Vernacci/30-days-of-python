# day-7 movie budget project

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000),
]

user_input = int(input("Type how many movies you want to add: "))

for _ in range(user_input):
    movie_name = input("Type the name of the movie: ")
    movie_budget = int(input("Type the budget used: "))
    new_movie = (movie_name, movie_budget)
    movies.append(new_movie)


budgets = []
movie_title = []

for a in movies:
    budgets.append(a[1])

average_budget = int(sum(budgets) / len(budgets))
int(average_budget)
print(f"Average budget is: {average_budget}")
print("---------------------------")


for b in movies:
    if b[1] > average_budget:
        movie_title.append(b[0])

print(f"These movies went above the average budget: {', '.join(movie_title)}")
print("------------------------")
print(f"{len(movie_title)} movies in total went above the average budget")
