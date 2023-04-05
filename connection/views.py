
from .models import *
from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib import auth, messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required


from .forms import *

# Create your views here.



def trackGrowth(request):
    obj = GrowthTrack.objects.all()
    context ={'obj':obj}
    return render(request,'connection/growth.html',context)