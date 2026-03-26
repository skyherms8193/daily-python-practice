"""
Kata: Add Movies to a Collection

Description:
Create a function that accepts a movie ID, title, director,
year, and genre. The function should store each movie as a
dictionary and add it to a list. Each time a movie is added,
the function should print the movie title.

This example adds 5 movies to the collection.

Concepts practiced:
- Defining functions with parameters
- Using dictionaries
- Storing dictionaries in a list
- Appending items to a list
- Printing values from a function

Notes:
Practicing how to organize related data using dictionaries.
This also reinforces how functions can create and store
structured information.
"""

movies = []

def add_movie(movie_id, title, director, year, genre):
    movie = {
        "id": movie_id,
        "title": title,
        "director": director,
        "year": year,
        "genre": genre
    }

    movies.append(movie)
    print(title)


# Add 5 movies
add_movie(1, "The Lion King", "Roger Allers & Rob Minkoff", 1994, "Animation")
add_movie(2, "Legally Blonde", "Robert Luketic", 2001, "Comedy")
add_movie(3, "Argo", "Ben Affleck", 2012, "Drama")
add_movie(4, "Apollo 13", "Ron Howard", 1995, "Drama")
add_movie(5, "Passport to Paris", "Alan Metter", 1999, "Comedy")


# Example output of full collection
print("\nMovie Collection:")
for movie in movies:
    print(movie)
