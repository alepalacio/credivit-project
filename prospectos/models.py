from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tags.tags import *

# Create your models here.

class Prospect(models.Model):
    salesman = models.ForeignKey(User, on_delete=models.CASCADE)
    prospect_name = models.CharField(max_length=120)
    nss = models.BigIntegerField(unique=True)
    birth_date = models.DateField(blank=True)
    facebook_user = models.CharField(max_length=120)
    phone_number = models.BigIntegerField(blank=True)
    total_amount = models.FloatField(help_text='Contaria con', max_length=20)
    sub_viv = models.FloatField(help_text='Sub vivienda', max_length=20)
    monthly_discount = models.FloatField(help_text='Descuento mensual', max_length=20)
    eco = models.FloatField(help_text='Ecotecnologias', max_length=20)
    call_info = models.TextField(blank=True, default="")
    status = models.CharField(max_length=40, choices=STATUS, default="Pending call")
    attention = models.CharField(max_length=120, default='Chava')
    prospect_user = models.CharField(help_text='Contacto de', max_length=60, choices=CONTACT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.prospect_name} - NSS: {self.nss} / {self.created_at.strftime('%d/%m/%Y')}"
    
    def get_absolute_url(self):
        return reverse('prospectos:detail', kwargs={'pk':self.pk})