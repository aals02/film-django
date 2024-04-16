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
from django.urls import path
from filmsearch.views import userProfile, movie_List, friendList, signUp, login
from .views import login_view, redirect_to_homepage
from . import views


urlpatterns = [
    path('', views.home),
    path("admin/", admin.site.urls),
    path("profile/", userProfile, name="userProfile"),
    path('movies/', movie_List, name='movie-list'),
    path("profile/", userProfile, name="userProfile"),
    path("signup/", signUp, name="signup"),
    path("login/", login, name="login")
    path('', redirect_to_homepage, name='home'),
    path('accounts/', include('accounts.urls'))
    # path('login/', views.login, name='login')  # you can use Django’s built-in view
]
