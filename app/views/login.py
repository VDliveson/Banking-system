from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from app.models import Customer


class LoginView(View):
    def get(self,request):
        customer=request.session.get('customer')
        if (customer):
            return redirect('home')
        else:
            return render(request,'login.html')
        
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        
        if(username == '' or password == ''):
            messages.error(request, 'Empty fields')
            return render(request, 'login.html')
        
        elif (request.POST['username']=='admin' and request.POST['password']=='admin'):
            return redirect('/admin')
        else:
            customer=Customer.get_Customer_by_login_id(username)

            if customer:
                flag=check_password(password,customer.password)
                if flag:
                    request.session['customer']=customer.customer_id
                    messages.success(request, 'Login successful')
                    return redirect('home')
                else:
                    messages.error(request,'Incorrect password')
            else:
                messages.error(request,'User does not exist, try contacting admin')
            return render(request,'login.html')
            
            
def logout(request):
    messages.success(request, 'User logged out successfully')
    request.session.clear()
    return redirect('login')