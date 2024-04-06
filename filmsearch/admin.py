from django.contrib import admin

# Register your models here.
from .models import Film
from .models import User

admin.site.register(Film)
admin.site.register(User)
