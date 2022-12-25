from django.db import models
import string
import random
from django.contrib.auth.models import User

# Create your models here.

def generate_unique_code():
    length=6
    while True:
        code = ''.join(random.choices(string.ascii_lowercase, k=length))
        if User.objects.filter(uid=code).count() == 0:
            break

    return code
