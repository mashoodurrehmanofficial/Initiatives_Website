
from django.http.request import HttpRequest
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from accounts.geodata import geodata
from django.views.decorators.csrf import csrf_exempt

import uuid,json
from root.models import *
from dateutil import parser

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


def create_initiative(request):
    return render(request,'dashboards/create_initiative.html', {
        "page_title":"Create Initiative"
    })


def submit_initiative(request): 
    title       = request.GET['title'] 
    description = request.GET['description'] 
    place_name  = request.GET['place_name'] 
    longitude   = request.GET['longitude'] 
    latitude    = request.GET['latitude'] 
    event_date  = request.GET['event_date'] 
    try:date_object = parser.parse(event_date).date()
    except:JsonResponse({"status":"date_error"})
    owner       = request.user
    Initiative_Table(
            title       = title,
            description = description,
            place_name  = place_name,
            longitude   = longitude ,
            latitude    = latitude,
            event_date  = event_date,
            date_object = date_object,
            owner       = owner
    ).save()
    return JsonResponse({"status":True})

def my_initiatives(request):
    initatives = Initiative_Table.objects.filter(owner=request.user).order_by('-id')
    return render(request,'dashboards/my_initiatives.html', {
        "page_title":"My Initiatives",
        'my_initiatives':initatives
    })



@csrf_exempt
def update_initiative(request,id):
    initative = Initiative_Table.objects.get(id=id)
    if request.method == 'POST':
        title       = request.POST['title'] 
        description = request.POST['description'] 
        place_name  = request.POST['place_name'] 
        longitude   = request.POST['longitude'] 
        latitude    = request.POST['latitude'] 
        event_date  = request.POST['event_date'] 
        object      = request.POST['object'] 
        try:date_object = parser.parse(event_date).date()
        except:JsonResponse({"status":"date_error"}) 
        initative.title = title
        initative.description = description
        initative.place_name = place_name
        initative.longitude = longitude
        initative.latitude = latitude
        initative.event_date = event_date
        initative.date_object = date_object
        object = json.loads(object)
        # print(object['context'][-2]['text_en-US'])
        initative.save()
        return JsonResponse({"status":False})

    return render(request,'dashboards/update_initiative.html', {
        "page_title":"Update Initiative",
        'initiative':initative
    })

def fetch_initiatives(request):
    initiatives = Initiative_Table.objects.all().order_by('date_object')
    print(initiatives)
    return render(request,'root/index.html', {
        "page_title":"All Initiative",
        'initiatives':initiatives
    })