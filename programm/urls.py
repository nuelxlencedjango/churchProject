
from django.urls import path
from .views import *
from . import views




app_name = 'programm'
urlpatterns =[
    path('',views.index, name='home'),
    path('giving/',views.donation, name='giving'),
    path('transact/',views.transaction, name='transact'),
    path('success/',views.successfulTransaction, name='success'),
    path('church_event/',views.churchEvent,name='church_event'),
 
    path('checkout/',views.checkout_session,name='checkout'), 
    path('success/',views.paysuccess,name='success'), 
    path('cancel/',views.cancel_pay,name='cancel'), 

    path('pastors/',views.pastorsInfo,name='pastors'),
    path('stories/',views.churchStory,name='stories'),

     path('val/',views.ourValues,name='val'),
    path('contact/',views.contactUs,name='contact'),
    path('mission/',views.ourMission,name='mission'),
    path('belief/',views.ourBelief,name='belief'),
    path('resource/',views.resourceControl,name='resource'),
    
]

