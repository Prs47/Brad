from django.shortcuts import render
from .models import User,UserProfile

# Create your views here.

def login(request):
    return render(request, 'accounts/login.html',{})

def addeducation(request):
    return render(request, 'accounts/addeducation.html',{})

def addexperience(request):
    return render(request, 'accounts/addexperience.html',{})

def createprofile(request):
    return render(request, 'accounts/createprofile.html',{})

def dashboard(request):
    return render(request, 'accounts/dashboard.html',{})

def profile(request):
    user_profile = UserProfile.objects.get(id=1)
    return render(request, 'accounts/profile.html', {"user_profile": user_profile })

def profiles(request):
    return render(request, 'accounts/profiles.html',{})

def register(request):
    return render(request, 'accounts/register.html',{})

