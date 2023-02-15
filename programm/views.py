from django.shortcuts import render
from .models import *
# Create your views here.
# importing the function from utils



def index(request):
    obj = Motivation.objects.all()
    context={'obj':obj}
    return render(request, 'general/home.html',context)


def donation(request):
    return render(request, 'general/offering.html')
   