
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from .forms import *
from django.shortcuts import redirect
from .models import *
from programm.forms import *
from programm .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def registration(request):
    error = ''
    if request.user.is_authenticated:

        #return HttpResponseRedirect(reverse(''))
        pass

    form = SignUpForm()
    form2 = UserDetailForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form2 = UserDetailForm(request.POST, request.FILES)
        
        if form.is_valid() and form2.is_valid():
            user = form.save()
            partner = form2.save(commit=False)
            partner.user = user
            partner.save()

            #user.save()         
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
      
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, 'You have successfully registered for growth success.One of our pastors will contact you shortly.')
                
                return HttpResponseRedirect(reverse('accounts:success'))

            return HttpResponseRedirect(reverse('accounts:connect'))

        else:
            if User.objects.filter(username=request.POST['username']).exists():
                error = 'A customer with this username already exists'

            else:
                error = 'Your password is not strong enough or both password must be same'
        

    return render(request, 'account/register.html', context={'form': form, 'form2':form2,  'user': "Customer Register", 'error': error})





def loginPage(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
      
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('accounts:my-page'))

        else:
            return render(request, 'account/login.html', context={'form': form, 'user': "Customer Login", 'error': 'Invalid username or password'})
    return render(request, 'account/login.html', context={'form': form, 'user': "Customer Login"})





def activities(request):

    return render(request,'account/activities.html')


@login_required()
def logoutPage(request):
    logout(request)
    return redirect('')


@login_required()
def successPage(request):
    
    return render(request,'account/reg-success.html')   


