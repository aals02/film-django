# Create your views here.
from django.http import HttpResponse

from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the newly created user


            subject = 'Welcome to Our Site!'
            message = f'Hi {user.username}, thanks for registering at our site!'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, email_from, recipient_list)

            return redirect('home')  # Assuming 'home' is the name of your homepage URL
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
