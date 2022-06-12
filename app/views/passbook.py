from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from app.models import Customer,Account,Transaction
from django.db.models import Q

class PassbookView(View):
    def get(self, request):
        customer=Customer.get_Customer_by_id(request.session.get('customer'))
        if customer:
            accounts=Account.get_customer_accounts(customer)
            transactions=(Transaction.objects.filter(Q(from_account__in=accounts) | Q(to_account__in=accounts)).order_by('-transaction_date'))
            return render(request,'passbook.html',{'transactions':transactions,'accounts':accounts})
        else:
            return redirect('login')