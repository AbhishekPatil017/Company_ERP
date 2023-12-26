from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    
    is_admin=models.BooleanField('is_admin ',default=False)
    is_company=models.BooleanField('is_company ',default=False)


class Company(models.Model):
    
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=255,blank=True)
    address=models.CharField(max_length=140,blank=True)
    email=models.CharField(max_length=250,blank=True)
    website=models.CharField(max_length=255,blank=True)
    gst_no=models.CharField(max_length=60,blank=True)
    hsn_sac=models.CharField(max_length=60,blank=True)
    bank_details=models.CharField(max_length=30,blank=True)
    pan_details=models.CharField(max_length=12,blank=True)
    # company_image=models.CharField()


    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        
        if not self.user_id:
            username=self.name.lower().replace(' ','-')
            password='123456'

            user=User.objects.create_user(username=username,password=password)
            self.user=user
            

        super().save(*args,**kwargs)
        self.user.is_company=True   
        self.user.save()  