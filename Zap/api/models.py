from django.db import models
import string
import random

# Create your models here.

def generate_unique_code():
    length=6
    while True:
        code = ''.join(random.choices(string.ascii_lowercase, k=length))
        if User.objects.filter(code=code).count() == 0 or Stat.objects.filter(code=code).count() == 0:
            break
        
    return code

class User(models.Model):
    code=models.CharField(max_length=8,default=generate_unique_code ,unique=True)
    host=models.CharField(max_length=50, default=None)
    stat=models.CharField(default='', max_length=8 ,unique=True)#Status of the id of the charging station if engaged None if not engaged
    phone = models.IntegerField(unique=True)
    charge_stat = models.IntegerField(default=0,null=False)

class Stat(models.Model):
    stat = models.CharField(max_length=8,default=generate_unique_code ,unique=True)
    user = models.CharField(max_length=8, unique=True)
    long = models.DecimalField(max_digits=30, decimal_places=15)
    lat = models.DecimalField(max_digits=30, decimal_places=15)
    lock_stat = models.BooleanField(default=False)#status if lock is engaged or disengaged
