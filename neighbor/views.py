from django.shortcuts import render, redirect
from .forms import SignUpForm, ProfileForm, BusinessForm, PostForm
from .models import Profile, Business, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/login/')
def home(request):
    current_user = request.user
    businesses = Business.get_business()
    posts = Post.get_posts()

    return render(request, 'index.html', {'current_user': current_user, 'businesses': businesses, 'posts': posts})


def signup(request):
    name = 'Signup'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form, 'name': name})


@login_required(login_url='/login/')
def profile(request):
    current_user = request.user

    return render(request, 'profile.html', {'current_user': current_user, })
