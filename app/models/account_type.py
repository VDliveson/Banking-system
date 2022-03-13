from django.db import models

class AccountType(models.Model):
    account_type = models.CharField(max_length=20)
    
    def __str__(self):
        return self.account_type