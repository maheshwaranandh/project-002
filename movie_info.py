import requests

class MovieInfo:

    OMDB_API_KEY = "7b9f2f45"
    OMDB_API_BASE_URL = "http://www.omdbapi.com/"

    def get_movie_info(self, movie_name):
        params = {"apikey": self.OMDB_API_KEY, "t": movie_name}
        response = requests.get(self.OMDB_API_BASE_URL, params=params)
        data = response.json()

        if data.get("Response") == "False":
            return None

        title = data.get("Title")
        year = int(data.get("Year"))
        language = data.get("Language")
        imdb_rating = float(data.get("imdbRating"))
        tomato_rating = float(next(filter(lambda x: x["Source"] == "Rotten Tomatoes", data.get("Ratings", [])), {}).get("Value", "0%").replace("%", "")) / 10

        return Movie(title, year, language, imdb_rating, tomato_rating)

class Movie:

    def __init__(self, title, year, language, imdb_rating, tomato_rating):
        self.title = title
        self.year = year
        self.language = language
        self.imdb_rating = imdb_rating
        self.tomato_rating = tomato_rating

    def __str__(self):
        return f"{self.title} ({self.year}) - Language: {self.language}, IMDb Rating: {self.imdb_rating}, Rotten Tomatoes Rating: {self.tomato_rating}"
movie_info = MovieInfo()

movie_name = input("Enter a movie name: ")
movie = movie_info.get_movie_info(movie_name)

if movie is None:
    print(f"Movie '{movie_name}' not found.")
else:
    print(movie)
