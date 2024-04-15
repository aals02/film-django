from django.shortcuts import render, redirect
from .forms import UserForm
from .APIConnection import connect
from .models import Films

# Create your views here.

#  user profile view
from .models import User
def userProfile(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(' ') #send to profile page
    else:
        form = UserForm()
    return render(request, 'profileUser.html', {'form': form})

    # items = User.objects.all()
    # return render(request, 'profileUser.html', {'items': items})
# add query to add user data from form
# add query to get only user details of user that logged in

#  user friend list view
# from .models import User
# def friendList(request):
#     items = Friends.objects.all()
#     return render(request, 'listfilm.html', {'items': items})


def movie_List(request):

    api_films = connect()  # This should return a list of dictionaries

    # You might want to clear the Films table before repopulating it
    # Be cautious with this as it will delete all existing entries in the Films table
    # Films.objects.all().delete()

    # Create Films objects only if they don't already exist
    for film_data in api_films:
        poster_url = "https://image.tmdb.org/t/p/w500" + film_data['poster_path']
        print("poster_path:", film_data['poster_path'])  # This will print the poster_path from the API
        print("Poster URL:", poster_url)  # This will print the full URL

        film, created = Films.objects.get_or_create(
            name=film_data['original_title'],
            defaults={
                'description': film_data['overview'],
                'poster_image': poster_url
            }
        )

    films = Films.objects.all()

    print(api_films)
    return render(request, 'movieRecs.html', {'films': films})




