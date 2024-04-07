from django.db import models
from django.core.validators import MinLengthValidator
import datetime


# Create your models here.

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
class Moviepreference(models.Model):
    Yes = 'Y'
    No = 'N'
    MOVIE_CHOICES = (
        (Yes,'Yes'),
        (No,'No'),
    )
    movie_id = models.CharField(max_length=100, blank = False, null = False)
    user_id = models.CharField(max_length=100, blank = False, null = False)
    yes_no = models.CharField(max_length=3, choices=MOVIE_CHOICES,default=Yes)
    
    def __str__(self):
        return self.movie_id

# storing API

class APIstore(models.Model):
    movie_id = models.CharField(max_length=100, blank = False, null = False)
    genre_id = models.CharField(max_length=100, blank = False, null = False)
    
    def __str__(self):
        return self.movie_id




    
    


