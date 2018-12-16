from django.db import models



# Create your models here.
class customer(models.Model):
    id=models.IntegerField(primary_key='true',default=0)
    name=models.CharField(max_length=100, default='')
    username = models.CharField(max_length=100, default='')
    password=models.CharField(max_length=20, default='')




