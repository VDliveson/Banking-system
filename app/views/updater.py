from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from app.models import Customer,Account,Transaction
from .forms import MyForm

class UpdaterView(View):
    def get(self,request):
        customer=Customer.get_Customer_by_id(request.session.get('customer'))
        return render(request, 'updater.html',{'customer':customer})
    def post(self,request):
        customer=Customer.get_Customer_by_id(request.session.get('customer'))
        first_name=request.POST['first_name']
        address=request.POST['address']
        gender=request.POST.get('customer_gender', None)
        last_name=request.POST['last_name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        date_of_birth=request.POST['date_of_birth']
        print(gender)
        form=MyForm()
        update=False
        
        if(gender!=customer.gender):
            customer.gender=gender
            update=True

        if(first_name!=''):
            customer.first_name=first_name
            update=True
        if(last_name!=''):
            customer.last_name=last_name
            update=True
        if(email!=''):
            customer.email=email
            update=True
        if(mobile!=''):
            customer.mobile=mobile
            update=True
        if(address!=''):
            customer.address=address
            update=True
        
        if(date_of_birth!=''):
            customer.date_of_birth=date_of_birth
            update=True
        
        customer.register()
        if(not update):
            messages.error(request,'No data received')
        else:
            messages.success(request,'Information updated successfully')
        return render(request, 'updater.html',{'customer':customer,'form':form})
            
        
        
        
        