from django.urls import path,include
from .views import *

urlpatterns=[
    path('',home.Index.as_view(),name='home'),
    path('login',login.LoginView.as_view(),name='login'),
    path('reset',reset.ResetView.as_view(),name='reset')
]