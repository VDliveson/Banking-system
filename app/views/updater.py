from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from app.models import Customer,Account,Transaction

class UpdaterView(View):
    def get(self,request):
        customer=Customer.get_Customer_by_id(request.session.get('customer'))
        return render(request, 'updater.html',{'customer':customer})
    def post(self,request):
        customer=Customer.get_Customer_by_id(request.session.get('customer'))
        first_name=request.POST['first_name']
        address=request.POST['address']
        gender=request.POST['gender']
        last_name=request.POST['last_name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        pan_number=request.POST['pan_number']
        date_of_birth=request.POST['date_of_birth']
        
        print(first_name,last_name,address,gender,email,mobile,pan_number,date_of_birth)
        
        if(first_name!=''):
            customer.first_name=first_name
        if(last_name!=''):
            customer.last_name=last_name
        if(email!=''):
            customer.email=email
        if(mobile!=''):
            customer.mobile=mobile
        if(pan_number!=''):
            customer.pan_number=pan_number
        if(address!=''):
            customer.address=address
        if(gender!=''):
            customer.gender=gender
        if(date_of_birth!=''):
            customer.date_of_birth=date_of_birth
        customer.register()
        messages.success(request,'Information updated successfully')
        return render(request, 'updater.html',{'customer':customer})
            
        
        
        
        