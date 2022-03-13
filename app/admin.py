from django.contrib import admin
from .models import * 


admin.site.register(Account)
admin.site.register(Customer)
admin.site.register(AccountType)
admin.site.register(Transaction)