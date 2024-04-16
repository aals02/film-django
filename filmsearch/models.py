from django.db import models
from django.core.validators import MinLengthValidator
import datetime
#karen
from django.conf import settings

# user profile database
class User(models.Model):
    name = models.CharField(max_length=100, blank = False, null = False)
    dob = models.DateField(blank=False, null=False, default=datetime.date.today)
    username = models.CharField(validators=[MinLengthValidator(6)], max_length=100, blank = False, null = False)
    password = models.CharField(validators=[MinLengthValidator(8)], max_length=100, blank = False, null = False)
    email = models.EmailField(blank = False, null = False)
    
    def __str__(self):
        return self.name
    
# friend list
class Friends(models.Model):
    friend_name = models.CharField(max_length=100, blank = False, null = False)
    friend_username = models.CharField(max_length=100, blank = False, null = False)
    user_id = models.CharField(max_length=100, blank = False, null = False)
    friend_id = models.CharField(max_length=100, blank = False, null = False)

    def __str__(self):
        return self.friend_name

# movie preferences
# class Moviepreference(models.Model):
#     Yes = 'Y'
#     No = 'N'
#     MOVIE_CHOICES = (
#         (Yes,'Yes'),
#         (No,'No'),
#     )
#     movie_id = models.CharField(max_length=100, blank = False, null = False)
#     user_id = models.CharField(max_length=100, blank = False, null = False)
#     yes_no = models.CharField(max_length=3, choices=MOVIE_CHOICES,default=Yes)

class Moviepreference(models.Model):
    LIKE = 'Y'
    DISLIKE = 'N'
    MOVIE_CHOICES = (
        (LIKE, 'Yes'),
        (DISLIKE, 'No'),
    )
    movie_id = models.CharField(max_length=100, blank=False, null=False)
    user_id = models.CharField(max_length=100, blank=False, null=False)
    preference = models.CharField(max_length=3, choices=MOVIE_CHOICES, default=LIKE)

    def __str__(self):
        return f"{self.user_id} - {self.movie_id} - {self.preference}"



    def __str__(self):
        return self.movie_id

# storing API
class APIstore(models.Model):
    movie_id = models.CharField(max_length=100, blank = False, null = False)
    genre_id = models.CharField(max_length=100, blank = False, null = False)

    def __str__(self):
        return self.movie_id



    
#     def __str__(self):
#         return self.friend_name
class Films(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    poster_image = models.URLField(default='https://image.tmdb.org/t/p/w500/d5NXSklXo0qyIYkgV94XAgMIckC.jpg')
    def __str__(self):
        return self.name
