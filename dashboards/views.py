
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
from root.GLOBAL_FUNCTIONS import *



import uuid,json,ast
from root.models import *
from dateutil import parser

# Create your views here.

@login_required(login_url='/account/login/')
def user_profile(request): 
    profile = Profile.objects.filter(user=request.user).first() 
    context = {"profile":profile}
    if request.method=='POST': 
        orignal_name = request.POST['username'] 
        email = request.POST['email'] 
        password = request.POST['password']
        longitude = request.POST['longitude']
        latitude = request.POST['latitude']
        place_name = request.POST['place_name']
        city = request.POST['city']
        region = request.POST['region']
        country = request.POST['country']

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
                target_profile.latitude = latitude
                target_profile.longitude = longitude
                target_profile.place_name = place_name
                target_profile.city = city
                target_profile.region = region
                target_profile.country = country


                target_profile.save()
 

                login(request, target_user)
                profile = Profile.objects.filter(email=email).first()
                context = {"profile":profile}
                return  render(request, 'dashboards/user_profile.html',context=context)
                
            else: 
                context['error'] = "Email already exists !"
                return  render(request, 'dashboards/user_profile.html',context=context)
                     
                
    return  render(request, 'dashboards/user_profile.html',context=context)




def create_initiative(request):
    categories = Initiative_Category.objects.all()
    return render(request,'dashboards/create_initiative.html', {
        "page_title":"Create Initiative",'categories':categories
    })


def submit_initiative(request): 
    title       = request.GET['title'] 
    description = request.GET['description'] 
    place_name  = request.GET['place_name'] 
    latitude    = request.GET['latitude'] 
    longitude   = request.GET['longitude'] 
    category    = request.GET['category'] 
    event_date  = request.GET['event_date'] 
    try:date_object = parser.parse(event_date).date()
    except:JsonResponse({"status":"date_error"})
    owner       = request.user
    print(category)
    category    = Initiative_Category.objects.get(category=category)
    Initiative_Table(
            title       = title,
            description = description,
            place_name  = place_name,
            latitude    = latitude,
            longitude   = longitude ,
            category   = category ,
            event_date  = event_date,
            date_object = date_object,
            owner       = owner
    ).save()
    return JsonResponse({"status":True})

def my_initiatives(request):
    categories = Initiative_Category.objects.all().order_by("category").exclude(category__startswith='Green Area')
    initiatives = Initiative_Table.objects.filter(owner=request.user).order_by('-id')
    context = {
        "page_title":"All Initiative",
        'my_initiatives':initiatives,
        "categories":categories,
        "page_title":"My Initiatives"
    }
    return render(request,'dashboards/my_initiatives.html', context)



def initial_filter(request):
    date        = request.GET['date'] 
    category    = request.GET['category'] 
    all_data = Initiative_Table.objects.filter(owner=request.user)
    if date:
        date_object = parser.parse(date).date()
        all_data =  all_data.filter(date_object=date_object) 
 
    if category:
        if category=='All Initiatives':
            pass
        else:
            category = Initiative_Category.objects.get(category=category)
            all_data =  all_data.filter(category=category) 

    all_data = list(all_data.values())

    print("Total = ", len(all_data))

    return JsonResponse({
        "results": all_data
    })










@csrf_exempt
def update_initiative(request,id):
    initative = Initiative_Table.objects.get(id=id) 
    categories = Initiative_Category.objects.all()
    categories = [x for x in categories if x!=initative.category]
    if request.method == 'POST':
        title       = request.POST['title'] 
        description = request.POST['description'] 
        place_name  = request.POST['place_name'] 
        longitude   = request.POST['longitude'] 
        latitude    = request.POST['latitude'] 
        event_date  = request.POST['event_date'] 
        category      = request.POST['category'] 
        object      = request.POST['object'] 
        try:
            date_object = parser.parse(event_date).date()
        except:JsonResponse({"status":"date_error"})  
        category = Initiative_Category.objects.get(category=category)
 
        initative.title = title
        initative.description = description
        initative.place_name = place_name
        initative.latitude = latitude
        initative.longitude = longitude
        initative.category = category
        initative.event_date = event_date
        initative.date_object = date_object 
        # object = json.loads(object)
        # print(object['context'][-2]['text_en-US'])
        print(initative.category)
        initative.save()
        return JsonResponse({"status":True})
    
    return render(request,'dashboards/update_initiative.html', {
        "page_title":"Update Initiative",
        'initiative':initative,
        "categories":categories
    })

def Prepare_Main_page(request):
    initiatives = Initiative_Table.objects.all().order_by('date_object')
    categories = Initiative_Category.objects.all().order_by("category")
    context = {
         "page_title":"All Initiative",
        'initiatives':initiatives,
        "categories":categories,
    }
    if request.user.is_authenticated:    
        user = request.user
        profile = Profile.objects.filter(user=user)
        if profile:
            profile = profile.first()
            print(profile)
            context['longitude'] =  profile.longitude
            context['latitude'] =  profile.latitude
   
    return render(request,'root/index.html', context)








def error_page(request):
    return JsonResponse({})
   
    # return render(request,'root/index.html', context)




def my_initiatives_info(request):
    initiative_id = request.GET['id']
    target_initiative = Initiative_Table.objects.get(id=initiative_id) 
    participants = list(Profile.objects.filter(user__in=target_initiative.enrolled.all()).values())
    badges = list(Badges.objects.all().order_by('badge').values()) 

    participant_badge = Badges_Container.objects.filter(
        key = initiative_id,
        profile__in = Profile.objects.filter(email__in=[x['email'] for x in participants])
    )
    

    for participant in participants:
        if participant_badge:
            temp = [x.badge.badge for x in participant_badge if x.profile.email==participant['email']]
            if temp:
                participant['badge'] = temp[0] 
            else: 
                participant['badge']=None 
        else:
                participant['badge']='None'



    return JsonResponse({
        "results":participants,
        'badges':badges
    })



def set_badge_to_user(request):
    initiative_id = request.GET['initiative_id']
    user_id = request.GET['user_id']
    badge = request.GET['badge']
    badge = Badges.objects.filter(badge=badge).first()
    target_initiative = Initiative_Table.objects.get(id=initiative_id)  
    target_profile = Profile.objects.filter(id=user_id).first() 

    record = Badges_Container.objects.filter(profile=target_profile,key=initiative_id)
    if record.exists():
        print("-> Changed")
        print(record)
        record = record.first()
        record.badge = badge
        record.save()

    else:
        print("-> Added")
        record = Badges_Container(badge=badge,profile=target_profile,key=initiative_id)
        record.save()
        target_initiative.particiapnt_badges.add(record)





    return JsonResponse({ 
    })
    