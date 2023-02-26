
from .models import *

from django.db.models import Q 
from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib import auth, messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView ,CreateView, UpdateView


from .forms import *


def index(request):
    obj = Motivation.objects.all()
    context={'obj':obj}
    return render(request, 'general/home.html',context)



def donation(request):
    return render(request, 'general/offering.html')



def transaction(request):
    form = DonationAndOfferingForm()
    if request.method == "POST":
        form = DonationAndOfferingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Transaction was successful! Thank your for donations/offering!!")
            return redirect('programm:success')
        
        form = DonationAndOfferingForm(request.POST)
        context ={'form':form}
        return render(request, 'general/donationInfo.html', context)
    
    form = DonationAndOfferingForm()
    context ={'form':form}
    return render(request, 'general/donationInfo.html', context)
   


def successfulTransaction(request):
    return render(request, 'general/success.html') 


def churchEvent(request):
    prog = ChurchPrograms.objects.all()
    gallery = ChurchGallery.objects.all()
    context ={'prog':prog,'gallery':gallery}
    return render(request, 'general/event.html',context) 

