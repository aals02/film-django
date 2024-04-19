from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
# from .forms import UserForm
from .forms import SignUpForm
from .models import Films, User, Friends, MoviePreference, APIstore
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from .forms import PasswordResetRequestForm
from collections import Counter, defaultdict
from django.db.models import Sum, Case, Value, IntegerField, When, Subquery, Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

#aaliyah and samiya
# DONE, NEED TESTING - query to add friends
# DONE, NEED TESTING - query to fetch/display users friends


# rafi'ah and monica
# DONE - collect genre data from API including ID and genre name and saved to database
# DONE - collect data (Movie info) from API and save to database for user viewing
# DONE - recommendation queries ->
#          Dont show new movies that have alr been viewed
#          Show movies that have similar genre_ids
# DONE - store movies they have swiped right and left on - movie preferences
# DONE - query for adding movies to database
# DONE - Page for user swipes right on and left on and displaying it

# Xiaowei
# query for log in if username and password match user in database
# allowing user to edit profile - query to alter/update database
# DONE - forgot password part - send email to reset 
# DONE - validate password
# IDK - hashing passwords

# Alex
# Homepage
# FIXING - Login and Signup Page
# User Profile Page
# Add Friends Page

#  user profile view
def userProfile(request):
    if not request.user.is_authenticated:
         return HttpResponse('You must be logged in to view this page\nPress back to return to previous page', status=401)
    else:
        user = request.user
        return render(request, 'profileUser.html', {'user': user})

def add_friend(request):
    if request.method == 'POST':
        current_user_id = request.user.id
        friend_username = request.POST.get('friend_username')
        try:
            friend = User.objects.get(username=friend_username)
            
            if not Friends.objects.filter(user_id=current_user_id, friend_id=friend.id).exists():
                Friends.objects.create(
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
        friends = User.objects.filter(Q(pk__in=Subquery(items.values('friend_id'))))
        return render(request, 'friends_list.html', {'items': friends})
    else:
        return HttpResponse('You must be logged in to view this page\nPress back to return to previous page', status=401)

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


@login_required
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        user.username = request.POST['username']
        user.dob = request.POST['dob']
        user.save()
        return redirect('home')  # Redirect to a confirmation page or back to the profile
    else:
        return render(request, 'profileUser.html', {'user': user})

def redirect_to_homepage(request):
    return redirect('home')


def movie_List(request):
    if not request.user.is_authenticated:
        return HttpResponse('You must be logged in to view this page\nPress back to return to previous page', status=401)
    page = request.GET.get('page') or 1
    islike = request.GET.get('like')

    if islike is not None:
        user_id = request.user.id
        movie_id = request.GET.get('movie_id')
        if islike.lower() == 'true':
            movie_pref = MoviePreference.objects.create(
                movie_id = movie_id,
                user_id = user_id,
                like = True
            )
        else:
            movie_pref = MoviePreference.objects.create(
                movie_id = movie_id,
                user_id = user_id,
                like = False
            )
        movie_pref.save()
    user_preferences = MoviePreference.objects.filter(user_id=request.user.id)
    films = Films.objects.filter(~Q(pk__in=Subquery(user_preferences.values('movie_id')))).order_by('id')
    if not films:
        return redirect('recommendations')

    # Pagination
    paginator = Paginator(films, 1)  # 1 film per page

    try:
        films = paginator.page(int(page))
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        films = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        films = paginator.page(paginator.num_pages)

    next_page = films.next_page_number() if films.has_next() else films.number + 1
    return render(request, 'movieRecs.html', {'films': films, 'next_page' : next_page, 'movie' : films.object_list[0]})
     
def save_preference(request):
    if request.method == 'POST' and request.user.is_authenticated:
        movie_id = request.POST.get('movie_id')
        action = request.POST.get('action')

        # Map action to Like or Dislike
        preference = MoviePreference.LIKE if action == 'like' else MoviePreference.DISLIKE

        # Update or create the preference
        MoviePreference.objects.update_or_create(
            user_id=request.user.id,
            movie_id=movie_id,
            defaults={'preference': preference}
        )
        return redirect('movie-list')  # Redirect after POST to avoid resubmission
    else:
        return HttpResponse('You must be logged in to update preferences, press back to return to previous page', status=401)



def movie_preference(request):
    if request.user.is_authenticated:
        liked_movies = MoviePreference.objects.filter(user_id=request.user.id, preference=MoviePreference.LIKE)
        disliked_movies = MoviePreference.objects.filter(user_id=request.user.id, preference=MoviePreference.DISLIKE)
        return render(request, 'movie_preference.html', {'liked_movies': liked_movies, 'disliked_movies': disliked_movies})
    else:
        return HttpResponse('You must be logged in to view this page\nPress back to return to previous page', status=401)

def get_recommended_movies(user_id):
    prefered_movies_for_user = MoviePreference.objects.filter(user_id=user_id, like=True)
    prefered_movies_objs = Films.objects.filter(Q(pk__in=Subquery(prefered_movies_for_user .values('movie_id'))))
    postive_counter = Counter([genre_id['api_genre_id'] for movie in prefered_movies_objs for genre_id in movie.genres.values('api_genre_id')])
    
    prefered_movies_for_user = MoviePreference.objects.filter(user_id=user_id, like=False)
    prefered_movies_objs = Films.objects.filter(Q(pk__in=Subquery(prefered_movies_for_user .values('movie_id'))))
    negative_counter = Counter([genre_id['api_genre_id'] for movie in prefered_movies_objs for genre_id in movie.genres.values('api_genre_id')])
    
    counter = defaultdict(int)
    for k, v in postive_counter.items():
        counter[k] += v
    
    for k, v in negative_counter.items():
        counter[k] -= v

    films = Films.objects.all()
    films_with_score = films.annotate(
        score=Sum(
            Case(
                *[When(genres__api_genre_id=genre_id, then=Value(counter.get(genre_id, 0))) for genre_id in counter.keys()],
                default=Value(0),
                output_field=IntegerField()
            )
        )
    ).order_by('-score')
    return films_with_score

def recommended_movies(request):
    user_id = request.user.id
    films_with_score = get_recommended_movies(user_id)
    return render(request, 'recommendation.html', {'films': films_with_score, "header_title" : f"Films List: Based on Your Genre Preferences"})

def recommendation_friend(request):
    friend_id = request.GET.get('friend_id')
    friend_obj = User.objects.filter(id = friend_id).first()
    films_with_score = get_recommended_movies(friend_id)
    return render(request, 'recommendation.html', {'films': films_with_score, "header_title" : f"Recommendations for {friend_obj.username}"})

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

def home(request):
    return render(request, 'home.html')

