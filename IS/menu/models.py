from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    type = models.CharField(max_length=20)
    img = models.ImageField(upload_to='images/', default=None)
    
    
class Table_Order(models.Model):
    table=models.IntegerField()
    order= models.CharField()
