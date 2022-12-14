from django import forms
from .models import *
from django.utils.html import format_html

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ("name","price","type", "img")


class CustomF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, menu):
        return format_html("<img class='field-img' src='{}'> <br> {} - {}", menu.img.url, menu.name, menu.price)

class OrderForm(forms.ModelForm):
    ordermenu = CustomF(
            queryset = Menu.objects.all(),
            widget = forms.CheckboxSelectMultiple,
            label = "All menu"
    )
    class Meta:
        model = Table_Order
        fields = ["ordermenu"]
        label = {
            'ordermenu' : 'All menu'
        }
