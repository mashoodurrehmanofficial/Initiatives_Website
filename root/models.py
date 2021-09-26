from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete,post_save,pre_save
from django.dispatch.dispatcher import receiver
from datetime import datetime

 



class Profile(models.Model):
    email = models.CharField(max_length=10000,blank=True,default='')
    orignal_name = models.CharField(max_length=10000,blank=True,default='')
    password = models.CharField(max_length=10000,blank=True,default='')
    longitude = models.CharField(max_length=10000,blank=True,default='')
    latitude = models.CharField(max_length=10000,blank=True,default='')
    place_name = models.CharField(max_length=10000,blank=True,default='')
    city = models.CharField(max_length=10000,blank=True,default='')
    region = models.CharField(max_length=10000,blank=True,default='')
    country = models.CharField(max_length=10000,blank=True,default='')
    state = models.CharField(max_length=10000,blank=True,default='')
    reset_code = models.CharField(max_length=10000,blank=True,default='')
    generated_name = models.CharField(max_length=10000,blank=True,default='')
    user = models.OneToOneField(User,on_delete=models.CASCADE) 

    def __str__(self):
        return self.generated_name



@receiver(post_delete, sender=User)
def delete_profile(sender, instance, *args, **kwargs):
    target_profile = Profile.objects.filter(user=instance)
    if target_profile:
        target_profile.delete()
    else:
        print("fail")
        print(instance.email)

 

class Initiative_Category(models.Model):
    category        = models.CharField(max_length=10000,blank=True,default='')
    def __str__(self):
        return self.category

class Badges(models.Model):
    badge           = models.CharField(max_length=10000,blank=True,default='') 
    def __str__(self):
        return str(self.badge)

class Badges_Container(models.Model):
    key           = models.CharField(max_length=10000,blank=True,default='')
    badge = models.ForeignKey(Badges,on_delete=models.CASCADE,default=None)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,default=None)



class Initiative_Table(models.Model):
    title           = models.CharField(max_length=10000,blank=True,default='')
    description     = models.TextField(max_length=1000000,blank=True,default='')
    place_name      = models.CharField(max_length=1000000,blank=True,default='')
    longitude       = models.CharField(max_length=10000,blank=True,default='')
    latitude        = models.CharField(max_length=10000,blank=True,default='')
    event_date      = models.CharField(max_length=10000,blank=True,default='',null=True)
    date_object     = models.DateField(blank=True,null=True)
    category        = models.ForeignKey(Initiative_Category,on_delete=models.CASCADE,related_name="Category",default=None)
    is_green_area   = models.BooleanField(default=False,blank=True)
    owner           = models.ForeignKey(User,on_delete=models.CASCADE,related_name="owner",default=None)
    enrolled        = models.ManyToManyField(User, related_name="enrolled",blank=True)
    particiapnt_badges= models.ManyToManyField(Badges_Container,default=None)

    def __str__(self):
        return str(self.title)+ ' --> ' + str(self.category.category)
