from django import forms
from .models import *

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ("name","price","type", "img")
class CustomF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, menu):
        return str(menu.name) +"  "+str(menu.price)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Table_Order
        fields = ["ordermenu"]
    ordermenu = CustomF(
        queryset=Menu.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )