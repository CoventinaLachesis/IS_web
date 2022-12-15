from django.db import models

from authentication.models import CustomUser
# Create your models here.

class Menu(models.Model):
    
    type_CHOICES=(("D","Drink"),("I","Icecream"),("C","Cake"),("M","Muffin"),("Do","Donut"),("O","Other"),)
    
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    type = models.CharField(max_length=12,
                  choices=type_CHOICES,
                  default="Other")
    img = models.ImageField(upload_to='images/', default=None)
    
    def __str__(self):
        return self.name

class Table(models.Model):
    table_number=models.IntegerField()
    Use_by=models.OneToOneField(CustomUser,on_delete=models.CASCADE, null=True)

class Table_Order(models.Model):
    table_number=models.ForeignKey(Table,on_delete=models.CASCADE)
    ordermenu= models.ManyToManyField(Menu)
    
    def __str__(self):
        return str(self.table_number)
    

