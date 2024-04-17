from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
# from .forms import UserForm
from .forms import SignUpForm
from .models import Films, User, Friends, Moviepreference, APIstore
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from .forms import PasswordResetRequestForm


# Create your views here.

#aaliyah and samiya
# query for adding movies to databse user swipes right on and left on and displaying it
# query to add friends
# query to fetch/display users friends


# rafi'ah and monica
# collect data from API and save to database for user viewing
# recommendation queries
# Add save to your function to store movies they have swiped right and left on
# query for adding movies to databse user swipes right on and left on and displaying it - we did this just modify it little bit

# Xiaowei
# query for log in if username and password match user in database
# allowing user to edit profile - query to alter/update database
# forgot password part - send email to reset 
# validate password
# hashing passwords


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

def add_friend(request):
    if request.method == 'POST':
        current_user_id = request.user.id
        friend_username = request.POST.get('friend_username')
        try:
            friend = User.objects.get(username=friend_username)
            
            if not Friends.objects.filter(user_id=current_user_id, friend_id=friend.id).exists():
                Friends.objects.create(
                    friend_name=friend.name,
                    friend_username=friend.username,
                    user_id=current_user_id,
                    friend_id=friend.id
                )
                return redirect('friend_list')
            else:
                return HttpResponse('Friendship already exists!', status=409)
        except User.DoesNotExist:
            return HttpResponse('User not found!', status=404)
    else:
        return render(request, 'friendAdd.html')

 # user friend list view
def friendList(request):
    if request.user.is_authenticated:
        current_user_id = request.user.id
        items = Friends.objects.filter(user_id=current_user_id)
        return render(request, 'friends_list.html', {'items': items})
    else:
        return HttpResponse('You must be logged in to view this page', status=401)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            subject = 'Welcome to Our Site!'
            message = f'Hi {user.username}, thanks for registering at our site!'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, email_from, recipient_list)

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
    return redirect('movie-list')

class CustomPasswordResetView(PasswordResetView):
    form_class = PasswordResetRequestForm
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        self.extra_email_context = {'email': email}
        return super().form_valid(form)


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
    #karen
def update_movie_preference(request):
    if request.method == 'POST' and request.user.is_authenticated:
        movie_id = request.POST.get('movie_id')
        action = request.POST.get('action')

        # Map action to 'Y' or 'N'
        preference = Moviepreference.LIKE if action == 'like' else Moviepreference.DISLIKE

        # Update or create the preference
        Moviepreference.objects.update_or_create(
            user_id=request.user.id,
            movie_id=movie_id,
            defaults={'preference': preference}
        )
        return redirect('movie-list')  # Redirect after POST to avoid resubmission
    else:
        return HttpResponse('You must be logged in to update preferences', status=401)



def movie_preference(request):
    if request.user.is_authenticated:
        liked_movies = Moviepreference.objects.filter(user_id=request.user.id, preference=Moviepreference.LIKE)
        disliked_movies = Moviepreference.objects.filter(user_id=request.user.id, preference=Moviepreference.DISLIKE)
        return render(request, 'movie_preference.html', {'liked_movies': liked_movies, 'disliked_movies': disliked_movies})
    else:
        return HttpResponse('You must be logged in to view this page', status=401)


from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from .forms import PasswordResetRequestForm

class CustomPasswordResetView(PasswordResetView):
    form_class = PasswordResetRequestForm
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        self.extra_email_context = {'email': email}
        return super().form_valid(form)
