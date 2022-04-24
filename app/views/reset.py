from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from app.models import Customer

class ResetView(View):
    def get(self, request):
        return render(request, 'password_reset.html')
    
    def post(self, request):
        email = request.POST['email']
        if(email == ''):
            messages.error(request, 'Empty fields')
            return render(request, 'password_reset.html')
        else:
            customer = Customer.get_Customer_by_email(email)
            
            if customer:
                messages.success(request, 'Password reset link sent to your email')
                return render(request,'password_reset.html')
            else:
                messages.error(request, 'User does not exist, try contacting admin')
                return render(request, 'password_reset.html')
            