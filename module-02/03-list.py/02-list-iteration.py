"""
Iterating over a list in Python is straightforward. You can use a for loop to iterate through each item in the list.
"""

# Lists - Example-02

# Iterating over a list.
print("\n ---------- Movies List ----------")
movies = ["The Shawshank Redemption", "The Godfather",
          "Pulp Fiction", "Forrest Gump", "Inception"]

for movie in movies:
    print(movie)


print("\n ---------- Index, plus Movies List ----------")
for index, movie in enumerate(movies):
    print(f"{index+1}. {movie}")


# ____________________________________________________________________

new_movie = ""

while new_movie != "Stop":
    new_movie = input("Introduce a new movie: ")

    if new_movie != "Stop":
        movies.append(new_movie)
print("\n ----------------- New movie list -----------------")
for index, movie in enumerate(movies):
    print(f"{index+1}. {movie}")
