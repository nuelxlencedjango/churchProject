
from django.urls import path
from .views import *
from . import views




app_name = 'programm'
urlpatterns =[
    path('',views.index, name='home'),
    path('giving/',views.donation, name='giving'),
    path('transact/',views.transaction, name='transact'),
    path('success/',views.successfulTransaction, name='success'),
 
]

