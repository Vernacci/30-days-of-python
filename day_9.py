# unpacking / destructuring

movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]

# enumarate
# for counter, (title, director, release) in enumerate(movies, start=1):
#     print(f'{counter}: {title} made by {director} released in {release}')

# zip function

pet_owners = ["Paul", "Andrea", "Marta"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]

# for owner, pet in zip(pet_owners, pets):
#     print(f'{owner} owns {pet}')


# exercicios

main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

# for character, actor, species in main_characters:
#      print(f'{character} is a {species.lower()} voiced by {actor}')


student = ("John Smith", 11743, ("Computer Science", "Mathematics"))

name, name_id, (major, minor) = student
print(name, name_id, major, minor)
