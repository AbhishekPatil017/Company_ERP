from django.db import models

# Create your models here.



class Customer(models.Model):

    CHOICES=(
        ('intern','Intern'),
        ('client','Client')
    )
    
    name=models.CharField(max_length=150)
    customer_type=models.CharField(max_length=120,choices=CHOICES)
    gst_number=models.CharField(max_length=120,blank=True,null=True)
    particulars=models.CharField(max_length=120,blank=True,null=True)
    address=models.CharField(max_length=120,blank=True,null=True)
    phone=models.CharField(max_length=120,blank=True,null=True)
    email=models.CharField(max_length=120,blank=True,null=True)
    registered_date=models.DateField(auto_now_add=True)
    joining_date=models.DateField()
    duration=models.CharField(max_length=120,blank=True,null=True)
    

    def __str__(self):
        return f'{self.name}'
    
class Invoice(models.Model):
     
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    invoice_no=models.CharField(max_length=10,default=0)
    invoice_date=models.DateField(auto_now_add=True) 
    amount=models.CharField(max_length=120,null=True,blank=True) 


    def __str__(self):
        return f'{self.customer.name}'

class Expense(models.Model):
    
    name=models.CharField(max_length=120)
    amount=models.CharField(max_length=120)
    date=models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.expense}'