import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','banking.settings')

import django
django.setup()

import random
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from app.models import Customer,Account,AccountType
import pandas as pd
import string

#Run this script as it is

#Customer generator

data=pd.read_csv('mock_data_new.csv')


for i in range(10):
    first_name=data.get('first_name')[i]
    last_name=data.get('last_name')[i]
    password=data.get('password')[i].lower()
    date_of_birth=data.get('date_of_birth')[i]
    email=data.get('email')[i]
    mobile=int(data.get('mobile')[i])
    address=data.get('address')[i]
    pan_number=data.get('pan_number')[i]
    # login_id=first_name[0:4]+str(random.randint(1111,9999))
    login_id=data.get('login_id')[i]
    gender=data.get('gender')[i]
    customer_id=data.get('customer_id')[i]
    # customer_id=str(''.join(random.choices(string.ascii_uppercase +string.digits, k = 8)))
    customer=Customer(first_name=first_name,last_name=last_name,date_of_birth=date_of_birth,
                      email=email,mobile=mobile,address=address,pan_number=pan_number,
                      login_id=login_id,customer_id=customer_id,gender=gender)
    customer.password=make_password(password)
    customer.register()
    print('Customer '+str(i)+' registered in db')
    

    
    
#Account generator

data=pd.read_csv('account_mock_data.csv')

for i in range(10):
    customer_id=Customer.get_Customer_by_id(data.get('customer_id')[i])
    account_type=AccountType.get_type_by_name(type=data.get('account_type')[i])
    balance=random.randint(500,10000)
    ifsc_code=data.get('ifsc_code')[i]
    account_number=data.get('account_number')[i]
    account=Account(customer_id=customer_id,account_type=account_type,
                    balance=balance,account_number=account_number,ifsc_code=ifsc_code)
    account.register()
    print('account' + str(i)+ ' registered in db')




# print(make_password('abcd'))