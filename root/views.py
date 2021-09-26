
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

# return  render(request, 'dashboards/user_profile.html',context=context)
def handler404(request, *args, **argv):
  return render(request,'root/404_page.html', {},status=404)
   
  


def handler500(request, *args, **argv):
    return render(request,'root/404_page.html', {},status=404)