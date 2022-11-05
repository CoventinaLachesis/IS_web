from tkinter import NONE
from django.db import models

# Create your models here.

class Menu(models.Model):
    
    type_CHOICES=(("Drink","D"),("Icecream","I"),("Cake","C"),("Muffin","M"),("Donut","Do"),("Other","O"),)
    
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    type = models.CharField(max_length=12,
                  choices=type_CHOICES,
                  default="Other")
    img = models.ImageField(upload_to='images/', default=None)
    
    def __str__(self):
        return self.name
    
class Table_Order(models.Model):
    table_number=models.IntegerField()
    ordermenu= models.ManyToManyField(Menu)
    
    def __str__(self):
        return str(self.table_number)
    

