from django.urls import path,include
from django.contrib.auth import views as auth_views 
from django.shortcuts import render
from .views import *

urlpatterns=[
    path('',home.Index.as_view(),name='home'),
    path('login',login.LoginView.as_view(),name='login'),
    path('logout',login.logout,name='logout'),
    path('passbook',passbook.PassbookView.as_view(),name='passbook'),
    path('portal',portal.PortalView.as_view(),name='portal'),
    path('updater',updater.UpdaterView.as_view(),name='updater'),
    path('captcha/', include('captcha.urls')),
    ]



    # path("password_reset", reset.password_reset_request, name="password_reset"),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
