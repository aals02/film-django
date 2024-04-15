from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from .forms import UserForm
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
    films = Films.objects.all()

    # Pagination
    paginator = Paginator(films, 1)  # 1 film per page
    page = request.GET.get('page')
    try:
        films = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        films = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        films = paginator.page(paginator.num_pages)

    return render(request, 'movieRecs.html', {'films': films})




