from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from app.models import Customer,Account,Transaction
from django.db.models import Q

class PassbookView(View):
    def get(self, request):
        customer=Customer.get_Customer_by_id(request.session.get('customer'))
        account=Account.get_customer_accounts(customer)[0]
        transactions=Transaction.objects.filter(Q(from_account=account) | Q(to_account=account)).order_by('-transaction_date')
        return render(request,'passbook.html',{'transactions':transactions,'account':account})
