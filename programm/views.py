from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    obj = Motivation.objects.all()
    context={'obj':obj}
    return render(request, 'general/home.html',context)
   