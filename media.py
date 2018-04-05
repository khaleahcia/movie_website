# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

#This file was created using instructions from Udacity.

import webbrowser

class Movie():
    """
    Class storing information about a movie.

    Args:
        title (str): Title of movies
        launch_date (str): Month and year movie was released
        poster_image (str): URL of movie poster from wikipedia
        trailer_youtube (str): URL of movie trailer on YouTube

    Attributes:
        title (str): Title of movies
        launch_date (str): Month and year movie was released
        poster_image_url (str): URL of movie poster from wikipedia
        trailer_youtube_url (str): URL of movie trailer on YouTube

    Methods:
        show_trailer (str): Opens youtube trailer
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, launch_date, poster_image, trailer_youtube):
        # initialize instance of class Movie
        self.title = movie_title
        self.launch_date = launch_date
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Opens the Youtube trailer of the movie

        Input:
            trailer_youtube_url (str): URL of movie trailer on youtube

        Behavior:
            Opens the webbrowser to display youtube movie trailer

        Returns:
            None.
        """
        webbrowser.open(self.trailer_youtube_url)
