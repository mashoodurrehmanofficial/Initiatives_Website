
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
from root.GLOBAL_FUNCTIONS import *
from dateutil import parser
from geopy import distance

 



def get_cluster(request): 
    latitude    = request.GET['latitude']
    longitude   = request.GET['longitude']
    radius      = request.GET['range_in_km'] 
    date        = request.GET['date'] 
    checked_catgories = request.GET['checked_catgories'] 
    if checked_catgories:
        checked_catgories = checked_catgories.split(',')
        

    print(longitude)

    if radius:radius = float(radius)
    else: radius     = 10
    center_point        = (latitude,longitude) 
    print("Center point -> ", center_point)
    print("Radius       -> ", radius)


    try:
        date_object = parser.parse(date).date()
        all_data =  Initiative_Table.objects.filter(date_object=date_object) 
    except:
        all_data =  Initiative_Table.objects.all() 
        print(all_data.count())
    if checked_catgories:
        all_data = all_data.filter(category__category__in=checked_catgories)
    # print('----',checked_catgories)

 

    cluster = [
        location for location in all_data.values() if(
            distance.distance(center_point, (location['latitude'],location['longitude'])).km <= radius
        )
    ] 

    def find_status(initiative_id):
        try: status = True if  [[z['id'] for z in y.enrolled.values() if z['id'] == request.user.id] for y in all_data.filter(id=initiative_id)] [0] else None
        except: status=None
        return status

    puer_cluster = [
       {**x, **{
           'enrolled': all_data.get(id=x['id']).enrolled.count(),
           "owner":Profile.objects.get(user=all_data.get(id=x['id']).owner).orignal_name,
           "my_status": find_status(x['id'])
           }
        } 
        for x in cluster
    ]
     
    # print(puer_cluster[0])
    print("--> Cluster Length = ",len(cluster))
    

    return JsonResponse({"results":puer_cluster})
    
def Handle_Membership(request):
    if request.user.is_authenticated:
        membership_status = request.GET['membership_status']
        initiative_id = request.GET['initiative_id']
        target_initiative = Initiative_Table.objects.get(id=initiative_id)
        target_user = request.user
        if membership_status=='join_btn':
            target_initiative.enrolled.add(target_user)
            enrolled = target_initiative.enrolled.count()
            return JsonResponse({"results":"added",'enrolled':enrolled})
        else:
            target_initiative.enrolled.remove(target_user)
            enrolled = target_initiative.enrolled.count()
            return JsonResponse({"results":"removed",'enrolled':enrolled})

        # print(membership_status)
        # print(initiative_id)
        # print(request.user)
    else:
        return JsonResponse({"results":"auth_error"})
        