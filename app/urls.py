from django.urls import path,include
from .views import *

urlpatterns=[
    path('',home.Index.as_view(),name='home')
]