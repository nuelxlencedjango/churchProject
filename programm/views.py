
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
from django.http import HttpResponse
import stripe
from django.conf import settings
import os
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
    prog = ChurchPrograms.objects.all().order_by('eventDate')
    gallery = ChurchGallery.objects.all().order_by('eventDate')

    context ={'prog':prog,'gallery':gallery}
    
    return render(request, 'general/event.html',context)  




def churchStory(request):
  
    return render(request, 'general/story.html') 





def pastorsInfo(request):
    title ="Search"

    pst = Pastors.objects.all()
    number  = Pastors.objects.all().count()
    

    #pagination
    page =request.GET.get('page', 1)
    paginator = Paginator(pst, 2)
    
    try:
        ourTeamPastors = paginator.page(page)

    except PageNotAnInteger:
        ourTeamPastors = paginator.page(1)

    except EmptyPage:   
        ourTeamPastors = paginator.page(paginator.num_pages)     


    context={'ourTeamPastors':ourTeamPastors,'number':number }  

    return render(request, 'pastors/abt_pastor.html',context)




def ourValues(request):
  
    return render(request, 'general/mission.html') 



def contactUs(request):
    form = ContactForm()
    if request.method =='POST':
        #get topic message ,message tittle,phone number,email address
        #form = ContactForm(request.POST)
        message_name = request.POST['name']
        phone = request.POST.get("phone" ,False)
        message_email = request.POST['email']
        message  = request.POST.get('message')
        topic = request.POST.get('phone')
        
        

        # seend a mail
        send_mail( 
            message_name,
            message_email, 
            message,

            [settings.EMAIL_HOST_USER],
        fail_silently=False)
        
        contacts = ContactUs()
        contacts.name =message_name
        contacts.phone = phone
        contacts.email = message_email
        contacts.topic = topic
        contacts.message = message
        contacts.save()
       
        return render(request, 'general/contact_us.html',{'message_name' :message_name}) 

    else:
        context={'form':form}
        return render(request ,'general/contact_us.html',context) 
   



def ourMission(request):
  
    return render(request, 'general/mission.html') 



def ourBelief(request):
  
    return render(request, 'general/belief.html') 



def paysuccess(request):
    return render(request, "success.html")   



def cancel_pay(request):
    return render(request, "cancel.html")   
                    


stripe.api_key=os.environ.get('STRIPE_API_KEY')
def checkout_session(request):
    if request.method == "POST":
        form = DonationAndOfferingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Thank you for your donations/offering. God bless you richly!!")
            #return redirect('programm:success')
            
            amt =int(request.POST.get('amount'))*100
            title =request.POST.get('title')
            session = stripe.checkout.Session.create(
            payment_method_types =['card'],
            line_items = [{
                        'price_data':{
                         'currency':'USD',
                          'product_data':{
                           'name':title,
                        },
                        'unit_amount':amt
                        },
                        'quantity':1,
                        }],
            mode ='payment',
            success_url = 'https://www.jesuschristglobalministries.com/success',
            cancel_url = 'https://www.jesuschristglobalministries.com/transact'
            )

            return redirect(session.url, code=303)

        
        form = DonationAndOfferingForm(request.POST)
        context ={'form':form}
        return render(request, 'general/donationInfo.html', context)
    
    
    

def resourceControl(request):

    return render(request, 'general/resources.html')



def upcomingEvent(request):
    events =UpcomingEvents.objects.all()
    context={'events':events}
    return render(request,'general/upcoming.html', context) 


def smallGroups(request):

    return render(request,'general/groups.html')