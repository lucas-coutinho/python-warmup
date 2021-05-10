from abc import ABC
from .utils import cos_sim
from .utils import pearson_corr

class User:
    """Defines an User entity.

    Attributes:
        id (int):
            numeric identifier.
        age (int):
            numeric age.
        occupation (string):
            the user's occupation.
        zip_code (int):
            numeric representation of the user's zip code.
    """
    def __init__(self, id: int,
                 age: int,
                 occupation: str,
                 zip_code: int,):
    
        self.id, self.age, self.occupation, self.zip_code = id, age, occupation, zip_code

    def classify_movie(self, movie, rate):
        raise NotImplemented()

    def mean_classification(self):
        raise NotImplemented()

    def similarity(self, other_user):
        raise NotImplemented()


class DistanceAlgorithm(ABC):
    """Abstract class for distance algorithms.
    """
    @abstractmethod
    def distance_between(self, item1, item2):
        raise NotImplemented()

class CossineDistance(DistanceAlgorithm):
    """Cossine distance of two `d`-dimensioned points.
    """
    def __call__(self, *items):
        item1= items[0]
        item2= items[1]

        return self.distance_between(item1, item2)

    def distance_between(self, item1, item2):
        
        return cos_sim(item1, item2)


class PearsonCorrelation(DistanceAlgorithm):
    """Pearson Correlation of two `d`-dimensioned points.
    """
    def __call__(self, *items):
        item1= items[0]
        item2= items[1]

        return self.distance_between(item1, item2)

    def distance_between(self, item1, item2):
        
        return pearson_corr(item1, item2)

class Movie:
    """Defines a Movie entity.

    Attributes:
        name (string):
            movie's name.
        release_date (string):
            release date formatted as mm/dd/yyyy.
        genre (string):
            movie's genre.
    """
    def __init__(self, name: str,
                 release_date: str,
                 genre: str,
    ):
        self.name, self.release_date, self.genre = name, release_date, genre

    def add_rating(self, rate):
        raise NotImplemented()

class Rating:
    """Defines a Rating entity.

    Attributes:
        rate (int):
            rating of a movie.
    """
    def __init__(self, rate: int):
        self.rate = rate
    

class Genre:
    """Defines a Genre entity.

    Attributes:
        genre (int):
            genre of a movie.
    """
    def __init__(self, genre: int):
        self.genre = genre
    
   
class RecommendationSystem:
    """Defines a Recommendation System entity.

    RS is the highest node in the recommendation system modelling.
    It is composed of users which have ratings and meta data.

    Attributes:
        name (string):
            recommendation system's name.
    """

    def __init__(self, name: str):
        self.name = name
