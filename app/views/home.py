from django.views import View
from django.shortcuts import redirect, render
from django.http import HttpResponse
from app.models import Customer,Account

class Index(View):
    def get(self, request):
        customer=Customer.get_Customer_by_id(request.session.get('customer'))
        if(customer):
            
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
            
            account_numbers=[]
            for i in range(len(accounts)):
                account_numbers.append(accounts[i].account_number)
            return render(request,'home.html',{'full_name':full_name,'date_of_birth':date_of_birth,
                                               'email':email,'mobile':mobile,
                                               'address':address,'login_id':login_id,
                                               'account_numbers':account_numbers,
                                               'total_balance':total_balance})
        else:
            return redirect('login')
            