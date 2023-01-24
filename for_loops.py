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
print("-----------------------------------")
# exercícios

employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00),
]

for employee in employees:
    total_pay = employee[1] * employee[2]
    print(f"employee: {employee[0]} is due to be paid {total_pay}")
