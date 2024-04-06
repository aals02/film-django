from django.db import models

# Create your models here.

# user profile database
class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    repeat_password = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
# friend list
# class Friends(models.Model):
#     friend_name = models.CharFields(max_length=100)
#     friend_username = models.CharFields(max_length=100)
    
#     def __str__(self):
#         return self.friend_name
