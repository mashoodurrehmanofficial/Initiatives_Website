from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete,post_save,pre_save
from django.dispatch.dispatcher import receiver


 



class Profile(models.Model):
    email = models.CharField(max_length=10000,blank=True,default='')
    orignal_name = models.CharField(max_length=10000,blank=True,default='')
    password = models.CharField(max_length=10000,blank=True,default='')
    country = models.CharField(max_length=10000,blank=True,default='')
    state = models.CharField(max_length=10000,blank=True,default='')



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


# @receiver(post_save, sender=User)
# def create_profile(sender, instance, *args, **kwargs):
#     target_profile = Profile.objects.filter(user=instance)
#     if not target_profile:
#         Profile()
#     else:
#         print("fail")
#         print(instance.email)






# @receiver(pre_delete, sender=User)
# def create_profile(sender, instance, *args, **kwargs):
#     Profile(user=User)
        


 