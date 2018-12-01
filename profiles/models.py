from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

User = get_user_model()

class Profile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,related_name='user_profile')
    first_name   = models.CharField(max_length=255, blank=True, null=True,default='Unknown')
    last_name  = models.CharField(max_length=255, blank=True, null=True,default='User')
    timestamp   = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='%Y/%m/%d',null=True,blank=True,default = 'ello.jpg')
    bio = models.CharField("Short Bio", max_length=200, blank=True, null=True,default='Write about yourself')

        

    def get_full_name(self):
        if self.first_name:
            return self.first_name

    def get_bio(self):
        if self.bio:
            return self.bio


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_handler(sender, instance, created, **kwargs):
    if not created:
        return
    # Create the profile object, only if it is newly created
    profile = Profile(user=instance)
    profile.save()
    

        
        
    