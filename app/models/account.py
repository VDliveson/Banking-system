from django.db import models

class Account(models.Model):
    acunt_number=models.CharField(max_length=15,primary_key=True)
    ifscoc_code=models.CharField(max_length=11,default='NULL')
    balance=models.DecimalField(max_digits=20,decimal_places=2)
    customer_id=models.ForeignKey('Customer',on_delete=models.CASCADE)
    account_type=models.ForeignKey('AccountType',on_delete=models.CASCADE)
    branch_name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.account_number