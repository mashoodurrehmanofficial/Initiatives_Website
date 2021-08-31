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

 


 

class Initiative_Table(models.Model):
    title       = models.CharField(max_length=10000,blank=True,default='')
    description = models.CharField(max_length=1000000,blank=True,default='')
    place_name    = models.CharField(max_length=1000000,blank=True,default='')
    longitude    = models.CharField(max_length=10000,blank=True,default='')
    latitude    = models.CharField(max_length=10000,blank=True,default='')
    event_date  = models.CharField(max_length=10000,blank=True,default='')
    date_object = models.DateField(blank=True)
    owner      = models.ForeignKey(User,on_delete=models.CASCADE,related_name="owner")
    enrolled    = models.ManyToManyField(User, related_name="enrolled")
    def __str__(self):
        return self.title

