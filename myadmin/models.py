from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_admin=models.BooleanField('is_admin ',default=False)
    is_company=models.BooleanField('is_company ',default=False)