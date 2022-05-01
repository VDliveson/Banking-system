from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from app.models import Customer,Account,Transaction
from datetime import datetime

class PortalView(View):
    def get(self, request):
        return render(request,'portal.html')
    
    def post(self, request):
        customer=Customer.get_Customer_by_id(request.session.get('customer'))
        ifsc_code=request.POST['ifsc_code']
        receiver_account=request.POST['receiver_account']
        
        sender_account=Account.get_customer_accounts(customer)[0]
        
        receiver_account=Account.get_customer_accounts_by_fields(receiver_account, ifsc_code)
        if(not receiver_account):
            messages.error(request, 'Account does not exist')
            return render(request, 'portal.html')
        else:
            print(customer, sender_account, receiver_account,'\n')
            money_to_transfer=request.POST['money_to_transfer']
            balance=sender_account.balance
            
            if int(money_to_transfer)>balance:
                messages.error(request,'Insufficient balance')
            elif (balance-int(money_to_transfer)<500):
                messages.error(request,'Minimum balance should be 500')
            else:
                transaction=Transaction(operation='+',from_account=sender_account,to_account=receiver_account,transferred_amount=money_to_transfer,transaction_date=datetime.now())
                sender_account.balance-=int(money_to_transfer)
                sender_account.register()
                receiver_account.balance+=int(money_to_transfer)
                receiver_account.register()
                transaction.register()
                messages.success(request,'Money transferred successfully')
        return render(request, 'portal.html')
            
            
            
        
        
            
    
        
        