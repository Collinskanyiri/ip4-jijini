from django.shortcuts import render, redirect
from .forms import SignUpForm, ProfileForm, BusinessForm, PostForm
from .models import Profile, Business, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
