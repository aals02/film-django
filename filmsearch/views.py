from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.utils.encoding import force_str
from .forms import UserForm
from .models import Films
from .models import User, Friends, Moviepreference, APIstore
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm





# Create your views here.
#  user profile view
from .models import User
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

#Aaliyah and samiya

# add query to add user data from form 
# add query to display/get user details of user thats logged in for profile
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

    
from django.shortcuts import redirect

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a success page.
            else:
                # Return an 'invalid login' error message.
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password.'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def redirect_to_homepage(request):
    return redirect('https://github.com/')




