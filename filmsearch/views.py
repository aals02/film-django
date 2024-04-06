from django.shortcuts import render

# Create your views here.

#  user profile view
from .models import User
def userProfile(request):
    items = User.objects.all()
    return render(request, 'listfilm.html', {'items': items})
# validation for objects like name

#  user friend list view
# from .models import User
# def friendList(request):
#     items = Friends.objects.all()
#     return render(request, 'listfilm.html', {'items': items})
