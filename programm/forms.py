from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import *






class DonationAndOfferingForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    amount = forms.DecimalField()
    title = forms.CharField()
    frequency = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    
    class Meta:
        model = DonationAndOffering
        fields =('amount','title','frequency','email','phone','first_name','last_name')

    
        Widget ={
          
            'first_name':forms.TextInput( attrs={'class':'form-control','placeholder':'First Name'}),
            #'middleName':forms.TextInput( attrs={'class':'form-control'}),
            'last_name':forms.TextInput( attrs={'class':'form-control'}),
            'amount':forms.NumberInput( attrs={'class':'form-control'}),
            'title':forms.TextInput( attrs={'class':'form-control'}),
            'frequency':forms.TextInput( attrs={'class':'form-control'}),
            'email':   forms.EmailInput( attrs={'class':'form-control'}),
           
            'phone':forms.TextInput(attrs={'class':'form-control'}),
           
           
            }
       
            
    #def __init__(self ,*args ,**kwargs):

     #   super(DonationAndOfferingForm,self).__init__(*args ,**kwargs)
      #  self.fields['title'].empty_label ="select title"