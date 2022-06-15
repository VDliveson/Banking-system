from django.db import models

class AccountType(models.Model):
    account_type = models.CharField(max_length=20,primary_key=True)
    
    def __str__(self):
        return self.account_type
    
    @staticmethod
    def get_type_by_name(type):
        try:
            return AccountType.objects.get(account_type=type)
        except:
            return False
    
     
    def register(self):
        self.save()