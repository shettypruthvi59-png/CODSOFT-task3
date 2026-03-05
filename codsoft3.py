movies = {
    "kgf": "action gangster gold crime",
    "kantara": "action thriller culture forest",
    "rajakumara": "family drama inspiration",
    "martin": "action thriller spy",
    "kd": "action historical drama",
    "tagaru": "action crime police gangster"
}

print("Kannada Movie Genre Finder")

movie = input("Enter a movie name: ").lower()

if movie in movies:
    print("Genre:", movies[movie])
else:
    print("Movie not found")