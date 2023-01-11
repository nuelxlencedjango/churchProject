from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    obj = Motivation.objects.all()
    context={'obj':obj}
    return render(request, 'hme.html',context)
    # return render(request, 'general/index.html',context)