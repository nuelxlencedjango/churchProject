
from django.urls import path
from .views import *
from . import views




app_name = 'programm'
urlpatterns =[
    path('',views.index, name='login'),
    path('giving/',views.donation, name='giving'),
 
]

