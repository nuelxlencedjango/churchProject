from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User


from .models import *

from django_countries.fields import CountryField
from cloudinary.models import CloudinaryField







class GrowthTrackRegistration(models.Model):
   
   user = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name='user_info')
   phone_no = models.CharField(max_length=500,null=True,blank=True)
   reg_date = models.DateField(auto_now_add=True)

   def __str__(self):
        return str(self.user)
