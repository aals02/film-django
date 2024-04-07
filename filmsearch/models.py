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
# class Friends(models.Model):
#     friend_name = models.CharFields(max_length=100, blank = False, null = False)
#     friend_username = models.CharFields(max_length=100, blank = False, null = False)
    
#     def __str__(self):
#         return self.friend_name
