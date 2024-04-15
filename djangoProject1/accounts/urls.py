from django.urls import path
from .views import login_view, redirect_to_homepage
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', login_view, name='login'),
    path('', redirect_to_homepage, name='home'),
    # path('login/', views.login, name='login')  # you can use Django’s built-in view
]