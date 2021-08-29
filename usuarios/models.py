from django.db import models
from tags.tags import *

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to='customers', default='no-picture.jpg')
    role = models.CharField(max_length=40, choices=ROLE, default="")
    
    def __str__(self):
        return str(self.name)