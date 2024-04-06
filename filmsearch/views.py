from django.shortcuts import render

# Create your views here.

from .models import Film

def filmlist(request):
    items = Film.objects.all()
    return render(request, 'listfilm.html', {'items': items})
def filmlist23(request):
    items = Film.objects.filter(name='abc')
    return render(request, 'listfilm.html', {'items': items})

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
