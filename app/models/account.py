from django.db import models
from .customer import Customer

class Account(models.Model):
    account_number=models.CharField(max_length=15,primary_key=True)
    ifsc_code=models.CharField(max_length=11,default='NULL')
    balance=models.DecimalField(max_digits=20,decimal_places=2)
    customer_id=models.ForeignKey('Customer',on_delete=models.CASCADE)
    account_type=models.ForeignKey('AccountType',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.account_number
    
    def register(self):
        self.save()
        
    @staticmethod
    def get_customer_accounts(customer_id):
        try:
            return Account.objects.filter(customer_id=customer_id)
        except:
            return []
        