from django.views import View
from django.shortcuts import redirect, render
from django.http import HttpResponse

class Index(View):
    def get(self, request):
        return render(request, 'home.html')