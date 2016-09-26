class Movie():
    """ Movie class is used for storing movie related information

        Attributes:
        title: Title of the movie
        summary: Brief summary of the movie plot
        poster_image_url: Link to the poster image of the movie
        trailer_youtube_url: Link to the youtube trailer of the movie
        
    """

    # Constructor for the class Movie
    def __init__(self, movie_title, movie_summary, movie_image,
               movie_trailer_url):
        self.title = movie_title
        self.summary = movie_summary
        self.poster_image_url = movie_image
        self.trailer_youtube_url = movie_trailer_url

        
        
