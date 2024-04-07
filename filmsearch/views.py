from django.shortcuts import render

# Create your views here.

#  user profile view
from .models import User
def userProfile(request):
    items = User.objects.all()
    return render(request, 'profileUser.html', {'items': items})
# validation for objects like name
# add query to add user data from form
# add query to get only user details of user thats logged in

#  user friend list view
# from .models import User
# def friendList(request):
#     items = Friends.objects.all()
#     return render(request, 'listfilm.html', {'items': items})
