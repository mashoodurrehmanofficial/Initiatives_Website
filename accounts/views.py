
from django.http.request import HttpRequest
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout


import uuid
from root.models import *
from .geodata import  geodata

# Create your views here.








def signup_page(request): 
    countries = [x['country'] for x in geodata] 
    if request.method=='POST': 
        orignal_name = request.POST['username'] 
        email = request.POST['email'] 
        password = request.POST['password']
        country = request.POST['country']
        state = request.POST['state']
        generated_name = orignal_name+"_"+str(uuid.uuid4())
        user = User.objects.filter(email=email)
        try:
            if user.exists():
                return render(request, 'accounts/signup.html',{"countries":countries,"error":"Email already exists !"})
            else:
                user = User(username=generated_name,password=make_password(password),email=email)
                user.save()     
                Profile(
                    generated_name=generated_name,orignal_name=orignal_name,
                    email=email,password=password,user=user,country=country,state=state
                ).save()

                return render(request, 'accounts/login.html',{"countries":countries,'message':"Account created successfully !"})
        except IntegrityError:
                return render(request, 'accounts/signup.html',{"countries":countries,"error":"Email has already been selected !"})
    
    return render(request, 'accounts/signup.html',{"countries":countries})



def login_page(request):
    if request.method=='POST':
        email = request.POST['email'] 
        password = request.POST['password']
        user = User.objects.filter(email=email)
        if user.exists():
            user = user.first()
            user_profile = Profile.objects.filter(user=user).first()
        
            user = authenticate(username=user_profile.generated_name,password=user_profile.password)
            if user is not None:
                login(request, user)
                print("login successful !") 
                return redirect('user_profile') 
            else:
                return render(request, 'accounts/login.html',{"error":"Sorry, Email or password is incorrect !"})
        else:
            print("dont exists")
            return render(request, 'accounts/login.html',{"error":"Sorry, Email or password is incorrect !"})
    return render(request, 'accounts/login.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')



def fetch_states(request):
    country = request.GET['country']
    states = [x['states'] for x in geodata if x['country'] == country]
    return JsonResponse({'states':states})





