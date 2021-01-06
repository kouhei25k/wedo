from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from accounts.models import CustomUser
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from accounts.form import *
# Create your views here.


def login_form(request):
    return render(request, 'accounts/login_form.html',)


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        # Redirect to a success page.
        return render(request, 'chat/index.html',)
        ...
    else:
        # Return an 'invalid login' error message.
        return render(request, 'accounts/login.html',)


def logout(request):

    return render(request, 'accounts/login.html',)


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,
                                password=raw_password)
            auth_login(request, user)
            return render(request, 'chat/index.html',)
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
