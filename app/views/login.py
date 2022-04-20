from django.views import View
from django.shortcuts import redirect, render
from django.http import HttpResponse

class LoginView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        if request.POST['username']=='admin' and request.POST['password']=='admin':
            return redirect('/admin')
        else:
            return HttpResponse('Invalid Credentials')