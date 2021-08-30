
from django.http.request import HttpRequest
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from accounts.geodata import geodata

import uuid
from root.models import *

# Create your views here.

@login_required(login_url='/account/login/')
def user_profile(request): 
    profile = Profile.objects.filter(user=request.user).first()
    countries = [x['country'] for x in geodata ] 
    cities = [x['cities'] for x in geodata if x['country']==profile.country][0]
    context = {"profile":profile,'countries':countries,'cities':cities}
    if request.method=='POST': 
        orignal_name = request.POST['username'] 
        email = request.POST['email'] 
        password = request.POST['password']
        country = request.POST['country']
        state = request.POST['state']

        user = User.objects.filter(email=request.user.email)
        if user.exists():
            user = user.first()
            if user.id==request.user.id:  
                generated_name = orignal_name+str(uuid.uuid4())
                
 
                user.username = generated_name
                user.set_password(password)
                user.email = email
                user.save()

                target_user = User.objects.get(email=user.email)
                target_profile = Profile.objects.get(user=target_user) 
                target_profile.orignal_name = orignal_name
                target_profile.generated_name = generated_name
                target_profile.email = email
                target_profile.password = password 
                target_profile.country = country
                target_profile.state = state
                target_profile.save()

                print(orignal_name)
                print(target_profile.orignal_name)
                print(target_profile)

                login(request, target_user)
                profile = Profile.objects.filter(email=email).first()
                countries = [x['country'] for x in geodata ] 
                states = [x['cities'] for x in geodata if x['country']==profile.country][0]

                context = {"profile":profile,'countries':countries,'cities':cities}
                return  render(request, 'dashboards/user_profile.html',context=context)
                
            else: 
                context['error'] = "Email already exists !"
                return  render(request, 'dashboards/user_profile.html',context=context)
                     
                
    return  render(request, 'dashboards/user_profile.html',context=context)


