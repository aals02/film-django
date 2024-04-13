from django.shortcuts import render
from .forms import UserForm
from .models import User, Friends, Moviepreference, APIstore

#  user profile view
def userProfile(request):
    # if request.method == 'POST':
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('') #send to profile page
    # else:
    #     form = UserForm()
    # return render(request, 'profileUser.html', {'form': form})

     items = User.objects.all()
     return render(request, 'profileUser.html', {'items': items})

 # user friend list view
def friendList(request):
    items = Friends.objects.all()
    return render(request, 'listfilm.html', {'items': items})
    
def signUp(request):
    return render(request, 'singup.html')

def login(request):
    return render(request, 'login.html')


# add query to add user data from form
# add query to display/get user details of user thats logged in for profile
# validate password
# api queries
# query for adding movies to databse user swipes right on and left on
# query to fetch movies user said yes to
# query to add friends
# query to fetch/display users friends 
# query for log in if username and password match user in database
# forgot password part - send email to reset
# allowing user to edit profile - query to alter/update database


