
from django.urls import path
from .views import *
from . import views




app_name = 'accounts'

urlpatterns =[
    path('register/',views.registration, name='register'),
     path('login/',views.loginPage, name='login'),
     path('success/',views.successPage, name='success'),
     path('my-page/',views.activities, name='my-page'),
     
  
    
]

