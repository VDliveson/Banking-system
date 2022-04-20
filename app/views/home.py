from django.views import View
from django.shortcuts import redirect, render
from django.http import HttpResponse

class Index(View):
    def get(self, request):
        customer=request.session.get('customer')
        
        if not customer:
            return redirect('login')
        else:
            return render(request,'home.html')