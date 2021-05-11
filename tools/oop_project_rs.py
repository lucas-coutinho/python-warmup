from abc import ABC, abstractmethod
from utils import cos_sim
from utils import pearson_corr

__all__ = ["User"]

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

        self._similarity = DistanceCollection(self)

    def classify_movie(self, movie, rate):
        raise NotImplemented()

    def mean_classification(self):
        raise NotImplemented()
    
    @property
    def similarity(self):
        
        return self._similarity


class DistanceAlgorithm(ABC):
    """Abstract class for distance algorithms.
    """
    @abstractmethod
    def distance_between(self, item1, item2):
        raise NotImplemented()

class CossineDistance(DistanceAlgorithm):
    """Cossine distance of two `d`-dimensioned points.
    """
    def __call__(self, item1, item2):

        return self.distance_between(item1, item2)

    def distance_between(self, item1, item2):
        
        return cos_sim(item1, item2)


class PearsonCorrelation(DistanceAlgorithm):
    """Pearson Correlation of two `d`-dimensioned points.
    """
    def __call__(self, item1, item2):

        return self.distance_between(item1, item2)

    def distance_between(self, item1, item2):
        
        return pearson_corr(item1, item2)

class DistanceCollection:
    """Collection of distance functions.
    """
    def __init__(self, user1: User):
        self.user1 = user1

    def cos(self, user2):

        return CossineDistance()(self.user1, user2)

    def pearson(self, user2):

        return PearsonCorrelation()(self.user1, user2)


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


class Rating:
    """Defines a Rating entity.

    Attributes:
        rate (int):
            rating of a movie.
        movie (Movie):
            movie associeated to the rating.
        user (User):
            user associeated to the movie rating.
    """
    def __init__(self, rate: int,
                 movie: Movie,
                 user:  User,
    ):

        self.user, self.movie, self.rate = user, movie, rate

        

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
