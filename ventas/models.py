from django.db import models
from prospectos.models import Prospect
from .utils import generate_code

# Create your models here.

class Sale(models.Model):
    prospect = models.OneToOneField(Prospect, on_delete=models.CASCADE)
    price = models.FloatField(blank=True)
    details = models.TextField(default='No details')
    ok_date = models.DateField(blank=True)
    transaction_code = models.CharField(max_length=12, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        self.price = self.prospect.total_amount
        if self.transaction_code == "":
            self.transaction_code = generate_code()
        return super().save(*args,**kwargs)
    
    def __str__(self):
        return f"ID: {self.id}, Prospect: {self.prospect.prospect_name}, NSS: {self.prospect.nss}"
    
class CSV(models.Model):
    file_name = models.FileField(upload_to='csvs')
    activated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.file_name)