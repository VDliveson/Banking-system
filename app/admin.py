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
    list_display = ['account_number','customer_id']
    
class AdminCustomer(ImportExportModelAdmin):
    resource_class=CustomerResource
    import_id_fields = ('customer_id')
    list_display =['first_name','customer_id']
    
admin.site.register(Account,AdminAccount)
admin.site.register(Customer,AdminCustomer)
admin.site.register(AccountType)
admin.site.register(Transaction)