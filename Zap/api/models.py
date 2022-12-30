from django.db import models
from django.contrib.auth.models import User


# Create your models here.

def generate_unique_code():

    return None

class Wallet(models.Model):
    uid = models.ForeignKey(User, to_field="username",  on_delete = models.SET_NULL, null=True)
    wid = models.IntegerField(null=False, default=00, unique=True)  
    amount = models.IntegerField(default=0, null=False)
