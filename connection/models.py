from django.db import models
from accounts.models import *
from django.utils import timezone
from accounts.models import *
#from cloudinary.models import CloudinaryField




class GrowthTrack(models.Model):
    title = models.CharField(max_length=500,null=True,blank=True)
    startDate = models.DateTimeField(blank=True, null=True)
    endDate = models.DateTimeField(blank=True, null=True)
    detail_1 = models.CharField(max_length=500,null=True,blank=True)
    detail_2 = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self): 
        return self.title
    
    class Meta:
        verbose_name_plural='Growth Track'
        ordering = ['-startDate']



class GrowthTrackEvents(models.Model):
    startDate = models.DateTimeField(blank=True, null=True)
    startDate = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.startDate
    
    class Meta:
      verbose_name_plural='Growth Track Event'
      ordering = ['-startDate']