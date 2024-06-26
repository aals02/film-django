"""
URL configuration for film project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from filmsearch.views import (userProfile, signup, login_view,
                              movie_List, movie_preference, recommended_movies,
                              friendList, add_friend, recommendation_friend, remove_friend,
                              redirect_to_homepage, home, update_profile)
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    #path('accounts/', include('accounts.urls')),
    path("profile/", userProfile, name="userProfile"),
    path('movies/', movie_List, name='movie-list'),
    path('add-friend/', add_friend, name='add_friend'),
    path('friends/', friendList, name='friendList'),
    path('remove_friend/', remove_friend, name='remove_friend'),
    path("signup/", signup, name="signup"),
    path("login/", login_view, name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path("preferences/", movie_preference, name='movie-preferences'),
    path('', redirect_to_homepage, name='home'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('recommended_movies/', recommended_movies, name ='recommendations'),
    path('friend-recommendations/', recommendation_friend, name = 'friendsrecs'),
    path('home/', home, name = 'home'),
    path('update-profile/', update_profile, name='update_profile'),
]
