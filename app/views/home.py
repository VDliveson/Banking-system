from django.views import View
from django.shortcuts import redirect, render
from django.http import HttpResponse
from app.models import Customer,Account

class Index(View):
    def get(self, request):
        customer=Customer.get_Customer_by_id(request.session.get('customer'))
        accounts=Account.get_customer_accounts(customer)
        
        total_balance=0
        for i in accounts:
            total_balance+=i.balance
        
        full_name=customer.first_name+' '+customer.last_name
        date_of_birth=customer.date_of_birth.strftime("%d/%m/%Y")
        email=customer.email
        mobile=customer.mobile
        address=customer.address
        login_id=customer.login_id
        print(date_of_birth, email, mobile, address, login_id)
        
        account_numbers=[]
        for i in range(len(accounts)):
            account_numbers.append(accounts[i].account_number)
        
        
        
        if not customer:
            return redirect('login')
        else:
            return render(request,'home.html')