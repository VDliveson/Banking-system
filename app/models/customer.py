from django.db import models



class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    date_of_birth=models.DateField()
    email=models.EmailField(max_length=50)
    mobile=models.IntegerField()
    address=models.CharField(max_length=200)
    pan_number=models.CharField(max_length=20)
    login_id=models.CharField(max_length=50)
    customer_id=models.CharField(max_length=50,primary_key=True)
    GENDER_CHOICES=[('male', 'Male'), ('female', 'Female'),['Other','other']]
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    
    def register(self):
        self.save()
        
    @staticmethod
    def get_Customer_by_login_id(login_id):
        try:
            return Customer.objects.get(login_id=login_id)
        except:
            return False
    
    @staticmethod
    def get_Customer_by_email(email):
        try:
            return Customer.objects.filter(email=email)
        except:
            return False
        
    @staticmethod
    def get_Customer_by_id(id):
        try:
            return Customer.objects.get(customer_id=id)
        except:
            return False
    
    
    
        

    
    
