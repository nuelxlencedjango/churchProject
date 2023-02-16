from django.db import models
from django.utils import timezone
from uuid import uuid4
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




