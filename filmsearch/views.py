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
# add query to add user data from form
# add query to get only user details of user thats logged in

 # user friend list view
def friendList(request):
    items = Friends.objects.all()
    return render(request, 'listfilm.html', {'items': items})


