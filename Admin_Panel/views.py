
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
import uuid,json
from root.models import *
from dateutil import parser




def adminpanel(request):
    return render(request,'admin_panel/adminpanel.html')



def manage_initiatives(request):
    all_initiatives = Initiative_Table.objects.all()
    return render(request,'admin_panel/manage_initiatives.html',{
        'all_initiatives':all_initiatives
    })





def mark_green(request):
    incoming_initiative = request.GET['id']
    incoming_initiative = Initiative_Table.objects.get(id=incoming_initiative)
    incoming_initiative.is_green_area  =  not incoming_initiative.is_green_area
    incoming_initiative.save()
    return JsonResponse({})




 







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
    
    return render(request,'admin_panel/update_initiative.html', {
        "page_title":"Update Initiative",
        'initiative':initative,
        "categories":categories
    })






def manage_green_areas(request):
    all_green_areas = Initiative_Table.objects.all() 
    all_green_areas=[x for  x in all_green_areas if x.category.category=='Green Area']

    return render(request,'admin_panel/manage_green_areas.html',{
        'all_green_areas':all_green_areas
    })



def create_green_area(request):
    categories = Initiative_Category.objects.filter(category__startswith='Green Area')
    return render(request,'admin_panel/create_green_area.html',{
        'categories':categories,
    })



@csrf_exempt
def update_green_area(request,id):  
    initative = Initiative_Table.objects.get(id=id) 
    categories = Initiative_Category.objects.all()
    categories = [x for x in categories if x!=initative.category]
    if request.method == 'POST':
        title       = request.POST['title'] 
        description = request.POST['description'] 
        place_name  = request.POST['place_name'] 
        longitude   = request.POST['longitude'] 
        latitude    = request.POST['latitude'] 
        # event_date  = request.POST['event_date'] 
        category      = request.POST['category'] 
        object      = request.POST['object'] 
        # try:
        #     date_object = parser.parse(event_date).date()
        # except:JsonResponse({"status":"date_error"})  
        category = Initiative_Category.objects.get(category=category)
 
        initative.title = title
        initative.description = description
        initative.place_name = place_name
        initative.place_name = place_name
        initative.latitude = latitude
        initative.longitude = longitude
        initative.category = category
        # initative.event_date = event_date
        # initative.date_object = date_object 
        # object = json.loads(object)
        # print(object['context'][-2]['text_en-US'])
        print(initative.category)
        initative.save()
        return JsonResponse({"status":True})
    
    return render(request,'admin_panel/update_green_area.html', {
        "page_title":"Update Initiative",
        'initiative':initative,
        "categories":categories
    })












def submit_green_area(request): 
    title       = request.GET['title'] 
    description = request.GET['description'] 
    place_name  = request.GET['place_name'] 
    latitude    = request.GET['latitude'] 
    longitude   = request.GET['longitude'] 
    category    = request.GET['category'] 
    # event_date  = request.GET['event_date'] 
    # try:date_object = parser.parse(event_date).date()
    # except:JsonResponse({"status":"date_error"})
    owner       = request.user 
    category    = Initiative_Category.objects.get(category__startswith=category)
    Initiative_Table(
            title       = title,
            description = description,
            place_name  = place_name,
            latitude    = latitude,
            longitude   = longitude ,
            category    = category ,
            is_green_area = True,
            # event_date  = event_date,
            # date_object = date_object,
            owner       = owner
    ).save() 
    return JsonResponse({"status":True})






def manage_accounts(request):
    all_accounts = Profile.objects.all()
    all_accounts = [
        x for x in all_accounts 
        if not x.user.is_superuser
    ]
    return render(request,'admin_panel/manage_accounts.html',{
        'all_accounts':all_accounts
    })

def update_profile(request,id):
    profile = Profile.objects.filter(user=User.objects.get(id=id)).first() 
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




        user = User.objects.filter(id=id)
        if user.exists():
            user = user.first()
            if user.id==int(id):  
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
                print(target_profile)
                profile = Profile.objects.filter(email=email).first()
                context = {"profile":profile}
                return  render(request, 'admin_panel/update_profile.html',context=context)
                
            else: 
                context['error'] = "Email already exists !"
                return  render(request, 'admin_panel/update_profile.html',context=context)
                     
        # return JsonResponse({})
                
    return  render(request, 'admin_panel/update_profile.html',context=context)



    
 