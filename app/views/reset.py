from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages


class ResetView(View):
    def get(self, request):
        return render(request, 'reset.html')