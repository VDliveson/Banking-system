from django.db import models
from .account import Account

class Transaction(models.Model):
    trasaction_id=models.AutoField(primary_key=True,blank=True)
    operation=models.CharField(max_length=1)
    from_account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='sender')
    to_account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='receiver')
    transferred_amount=models.DecimalField(max_digits=20,decimal_places=2)
    transaction_date=models.DateTimeField()