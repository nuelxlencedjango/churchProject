from django.db import models
from django.utils import timezone
from uuid import uuid4
from cloudinary.models import CloudinaryField
# Create your models here.



class Motivation(models.Model):
    title = models.CharField(max_length=500,null=True,blank=True)
    mesg= models.TextField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.title
    


class DonationAndOffering(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    amount = models.DecimalField(decimal_places=5,max_digits=10)
    title = models.CharField(max_length=200)
    frequency = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=50,null=True, blank=True)
    date_paid = models.DateTimeField(blank=True, null=True)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return f"{self.first_name} - {self.title}"
    

    def save(self, *args, **kwargs):
        if self.date_paid is None:
            self.date_paid = timezone.localtime(timezone.now())

        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            
        super(DonationAndOffering, self).save(*args, **kwargs) 






class ChurchPrograms(models.Model):
    title = models.CharField(max_length=500,null=True,blank=True)
    mesg= models.TextField(max_length=500,null=True,blank=True)
    eventDate = models.DateTimeField(blank=True, null=True)
    img = CloudinaryField(blank=True,null=True)
    venue = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.title
    


class ChurchGallery(models.Model):
    title = models.CharField(max_length=500,null=True,blank=True)
    eventDate = models.DateTimeField(blank=True, null=True)
    img = CloudinaryField('pics',blank=True,null=True)
   

    def __str__(self):
        return self.title
    
    class Meta:
      verbose_name_plural='Church Gallery'
      ordering = ['-eventDate']
    



class ImageGallery(models.Model):
    eventImg = models.ForeignKey(ChurchGallery,on_delete=models.SET_NULL, null=True, blank=True, related_name="images_church")
    img = CloudinaryField('images',blank=True,null=True)
    #dateTime =models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.eventImg

    class Meta:
      verbose_name_plural='Image Gallery'
      ordering = ['-eventImg']





class Pastors(models.Model):
    fullname = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    img = CloudinaryField(blank=True,null=True)
    description2 = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.fullname} - {self.title}"
    
 


class UpcomingEvents(models.Model):
    event_name = models.CharField(max_length=200)
    startDate =models.DateField()
    endDate = models.DateTimeField(blank=True, null=True)
    timing =models.TimeField()
    venue = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    img = CloudinaryField(blank=True,null=True)
   
    
    
    def __str__(self):
        return f"{self.event_name} - {self.venue}"    