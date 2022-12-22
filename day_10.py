# dictionaries

student = {
    "name": "Victor",
    "age": 19,
    "major": "Computer Science",
    "grades": [80, 90, 99]
}

# add a key
student["hobby"] = "gaming"
# print(student)

# modify existing values
student["age"] = 20


# updating a dictionarie
movie = {
    "title": "Avengers: Endgame",
    "directors": ["Anthony Russo", "Joe Russo"],
    "year": 2019
}

meta_info = {
    "runtime": 181,
    "budget": "$356 million",
    "earnings": "$2.798 billion",
    "producer": "Kevin Feige"
}

movie.update(meta_info)

# deleting values
del movie["year"]

# iteration
# for key, value in movie.items():
#     print(f'{key}: {value}')

# exercicios

album = {
    "title": "The dark side of the moon",
    "band": "Pink Floyd",
    "release": 1973,
    "tracks":  (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
}

for key, value in album.items():
    print(f'{key}: {value}')

del album["tracks"]
del album["release"]
album["release"] = "march 1st 1973"
print(album)
