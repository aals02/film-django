from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Films
from .models import User, Friends, Moviepreference, APIstore
from django.contrib.auth.decorators import login_required



# Create your views here.
#  user profile view
from .models import User
def userProfile(request):
    # #def userProfile(request):
    # # Access the logged-in user's details
    # if request.method == 'POST':
    #     form = UserForm(request.POST, instance=request.user)  # Pass instance to populate the form with user data
    #     if form.is_valid():
    #         form.save()
    #         return redirect('profile_view')  # Redirect to a named profile view
    # else:
    #     form = UserForm(instance=request.user)  # Initialize the form with user data for GET request

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

#Aaliyah and samiya
# query for adding movies to databse user swipes right on and left on
# allowing user to edit profile - query to alter/update database
# query to fetch movies user said yes to
# query to add friends
# query to fetch/display users friends

# rafi'ah and monica
# recommendation queries

# Xiaowei

# query for log in if username and password match user in database
# forgot password part - send email to reset
# validate password
# hashing passwords




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


# def update_movie_preference(request):
#     if request.method == 'POST':
#         movie_id = request.POST.get('movie_id')
#         action = request.POST.get('action')

#         # Check valid action
#         if action not in ['like', 'dislike']:
#             return HttpResponse('Invalid action', status=400)

#         # Map action to 'Y' or 'N'
#         yes_no = Moviepreference.Yes if action == 'like' else Moviepreference.No

#         # Update or create the preference
#         Moviepreference.objects.update_or_create(
#             user_id=request.user.id,  # Assuming you are using Django's authentication system
#             movie_id=movie_id,
#             defaults={'yes_no': yes_no}
#         )
#         return redirect('some-view-name')  # Redirect after POST to avoid resubmission
#     else:
#         return HttpResponse('Method not allowed', status=405)

