# Movie class that takes title, image url and youtube trailer url as the parameters
class Movie:
    '''
    Class to store details about movie object.

    Attributes:
        title (str): Title of the movie
        poster_image_url (str): The url for the poster for the movie
        trailer_youtube_url (str): The url for the youtube trailer for the movie
    '''
    # Constructor to intialize the class with the arguments given.
    def __init__(self, movie_title, poster_image, trailer_youtube_url):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url

