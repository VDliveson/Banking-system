from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from app.models import Customer,Account,Transaction

class UpdaterView(View):
    def get(self,request):
        return render(request, 'updater.html')