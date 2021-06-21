from faker import Faker
import random
fake = Faker("pl_PL")

# Do usunięcia polskich znaków:...........................................................................................


def normalize_letters(tekst):
    '''
    Źdźbło -> zdzblo
    '''
    text = tekst.lower()
    polish_letters = "ąćęłńóśźż"
    normal_letters = "acelnoszz"
    new_text = ""
    for i in text:
        letter = i
        if letter in polish_letters:
            letter = normal_letters[polish_letters.index(i)]
        new_text += letter
    return new_text


# Film:..................................................................................................................
class Movie():
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

        # variables:
        self._views = 0

    def __str__(self):
        return f"{self.title} ({self.year})"

    @property
    def views(self):
        return self._views

    @views.setter
    def views(self, value):
        if value >= 0:
            self._views = value
        else:
            raise ValueError(
                f"Podana wartość: {value} jest mniejsza od 0, a nie powinna.")

    def play(self):
        '''
        views +=1
        '''
        self.views += 1


# Serial:....................................................................................................................
class Serie(Movie):

    def __init__(self, title, year, genre, episode, season):
        super().__init__(title, year, genre)
        self.episode = episode
        self.season = season

    def __str__(self):
        season_str = f"0{self.season}"[-2:]
        episode_str = f"0{self.episode}"[-2:]
        return f"{self.title} S{season_str}E{episode_str}"


# Biblioteka filmów:............................................................................................................
class Biblioteca():

    def __init__(self):
        self._movies_list = []

    @property
    def movies_list(self):
        return self._movies_list

    def add_movie(self, movie):
        self.movies_list.append(movie)

    def get_movies(self):
        movies = []
        for movie in self.movies_list:
            if isinstance(movie, Movie) and not isinstance(movie, Serie):
                movies.append(movie)
                # print(movie)
        by_title = sorted(movies, key=lambda movie: movie.title)
        return by_title

    def get_series(self):
        movies = []
        for movie in self.movies_list:
            if isinstance(movie, Serie):
                movies.append(movie)
                # print(movie)
        by_title = sorted(movies, key=lambda movie: movie.title)
        return by_title

    def search(self):
        '''
        Search movie by title form user input.
        '''
        movies = []
        searched = input("Podaj tytuł filmu:\n")
        for movie in self.movies_list:
            if normalize_letters(movie.title) == normalize_letters(searched):
                movies.append(movie)
                print(movie)
        if len(movies) == 0:
            print("NO RESULTS")
        return movies

    def generate_views(self):
        '''
        Increases random movie views value by random value.
        '''
        random.choice(self.movies_list).views += random.randint(1, 100)

    def create_view_10_times(self):
        for i in range(10):
            self.generate_views()

    def top_titles(self, how_many=1, typ="all"):
        if typ == "movie":
            movies = self.get_movies()
        elif typ == "serie":
            movies = self.get_series()
        else:
            movies = self.movies_list
        by_views = sorted(movies, key=lambda movie: -movie.views)
        return by_views[0:min(how_many, len(by_views))]


# Wypróbowanie kodu:..........................................................................................................
base = []
base.append(Movie("Rejs", 1970, "Komedia"))
base.append(Movie("Prawo I Pięść", 1964, "Western"))
base.append(Movie("Krzyżacy", 1960, "Historyczny"))
base.append(Serie(
    "Stawka Większa Niż Życie", 1965, "Szpiegowski", 1, 1))
base.append(Serie(
    "Stawka Większa Niż Życie", 1965, "Szpiegowski", 2, 1))


biblioteka = Biblioteca()


for i in base:
    biblioteka.add_movie(i)

# for movie in biblioteka.movies_list:
 #   print(movie)
 #   print(type(movie))

print("\nFilmy:")
for i in biblioteka.get_movies():
    print(i)
print("\nSeriale:")
for i in biblioteka.get_series():
    print(i)
print("\nWyszukaj:")
biblioteka.search()
print("\nGenerate Views:")
biblioteka.generate_views()
for i in biblioteka.movies_list:
    print(f"{i}: {i.views}")

print("\n10 times:")
biblioteka.create_view_10_times()
for i in biblioteka.movies_list:
    print(f"{i}: {i.views}")

print("\nTop:")
criteria_list = ["all", "movie", "serie"]
for criteria in criteria_list:
    print(criteria)
    top = biblioteka.top_titles(3, criteria)
    for i in top:
        print(f"{i}: {i.views}")
