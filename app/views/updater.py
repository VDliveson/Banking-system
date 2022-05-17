from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from app.models import Customer,Account,Transaction
from .forms import MyForm
from django.contrib.auth.hashers import make_password, check_password

class UpdaterView(View):
    def get(self,request):
        customer=Customer.get_Customer_by_id(request.session.get('customer'))
        return render(request, 'updater.html',{'customer':customer})
    def post(self,request):
        customer=Customer.get_Customer_by_id(request.session.get('customer'))
        first_name=request.POST['first_name']
        address=request.POST['address']
        gender=request.POST.get('customer_gender', customer.gender)
        last_name=request.POST['last_name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        date_of_birth=request.POST['date_of_birth']
        password=request.POST.get('password')
        check_password=request.POST.get('check_password')
        form=MyForm()
        update=False
        passw=False
        
        if(gender!=customer.gender):
            customer.gender=gender
            update=True


        if(first_name!='' and first_name!=customer.first_name):
            customer.first_name=first_name
            update=True
        if(last_name!='' and last_name!=customer.last_name):
            customer.last_name=last_name
            update=True
        if(email!='' and email!=customer.email):
            customer.email=email
            update=True
        if(mobile!='' and mobile!=customer.mobile):
            customer.mobile=mobile
            update=True
        if(address!='' and address!=customer.address):
            customer.address=address
            update=True
        if(date_of_birth!='' and date_of_birth!=customer.date_of_birth):
            customer.date_of_birth=date_of_birth
            update=True
        if(password!=''):
            if(check_password==password):
                update=True
                customer.password=make_password(password)
                messages.success(request, 'Password changed successfully')
            else:
                messages.error(request, 'Password and confirm password fields do not match')
        
        if(not update):
            messages.error(request,'No data received')
        else:
            customer.register()
            messages.success(request,'Information updated successfully')
        return render(request, 'updater.html',{'customer':customer,'form':form})
            
        
        
        
        