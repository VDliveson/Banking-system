from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import * 

class CustomerResource(resources.ModelResource):
    class Meta:
        model=Customer

class AccountResource(resources.ModelResource):
    class Meta:
        model=Account
class AdminAccount(ImportExportModelAdmin):
    resource_class=AccountResource
    
class AdminCustomer(ImportExportModelAdmin):
    resource_class=CustomerResource
    
admin.site.register(Account,AdminAccount)
admin.site.register(Customer,AdminCustomer)
admin.site.register(AccountType)
admin.site.register(Transaction)