
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

# Create your views here.


def user_profile(request):
    return  render(request, 'dashboards/user_profile.html',{"password":"password"})


