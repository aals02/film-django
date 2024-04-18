from django.db import models
from django.core.validators import MinLengthValidator
import datetime
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# user profile database
class User(AbstractUser):
    name = models.CharField(max_length=100, blank = False, null = False)
    dob = models.DateField(blank=False, null=False, default=datetime.date.today)
    # username = models.CharField(validators=[MinLengthValidator(6)], max_length=100, blank = False, null = False)
    # password = models.CharField(validators=[MinLengthValidator(8)], max_length=100, blank = False, null = False)
    # email = models.EmailField(blank = False, null = False)
    
# friend list
class Friends(models.Model):
    friend_name = models.CharField(max_length=100, blank = False, null = False)
    friend_username = models.CharField(max_length=100, blank = False, null = False)
    user_id = models.CharField(max_length=100, blank = False, null = False)
    friend_id = models.CharField(max_length=100, blank = False, null = False)

    def __str__(self):
        return self.friend_name


# storing API
class APIstore(models.Model):
    movie_id = models.CharField(max_length=100, blank = False, null = False)
    genre_id = models.CharField(max_length=100, blank = False, null = False)

    def __str__(self):
        return self.movie_id



    
#     def __str__(self):
#         return self.friend_name
class Genre(models.Model):
    api_genre_id = models.IntegerField(unique=True)
    genre_name = models.CharField(max_length=100)
    def __str__(self):
        return self.genre_name

class Films(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    genres = models.ManyToManyField(Genre)
    lang = models.CharField(default = 'en', max_length= 20)
    release_date = models.DateField(null=True, blank=True)
    rating = models.FloatField(default = 0.0)
    poster_image = models.URLField(default='https://image.tmdb.org/t/p/w500/d5NXSklXo0qyIYkgV94XAgMIckC.jpg')
    def __str__(self):
        return self.name

class MoviePreference(models.Model):
    movie_id = models.CharField(max_length=100, blank=False, null=False)
    user_id = models.CharField(max_length=100, blank=False, null=False)
    like = models.BooleanField(default=True)

    def __str__(self):
        if self.like:
            preference = "like"
        else:
            preference = "dislike"
        return f"{self.user_id} - {self.movie_id} - {preference}"
