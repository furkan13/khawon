from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.conf import settings

# Create your models here.
class restaurant(models.Model):
    id=models.IntegerField(primary_key='true',default=0)
    name=models.CharField(max_length=100, default='')
    menu=models.ImageField(upload_to='media',blank=True)
    adresss=models.CharField(max_length=100)
    special_iteam=models.CharField(max_length=100)
    contact=models.IntegerField(default=0)
    logo = models.ImageField(upload_to='media/logo', blank=True)
    tag=models.CharField(default='',max_length=500)
    location=models.CharField(default='',max_length=100)









