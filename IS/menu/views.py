from django.shortcuts import render
from django.contrib.auth import get_user_model

from .forms import *

User = get_user_model()

# Create your views here.

def order(request,table):
    if request.method == 'POST':
        
        menu=OrderForm(request.POST,request.FILES)
        if menu.is_valid():
            if not Table.objects.filter(table_number=table):
                print("new")
                if request.user.is_authenticated:                
                    Table.objects.create(table_number=table,Use_by=request.user)
                else:
                    Table.objects.create(table_number=table)
            
            item= menu.cleaned_data['ordermenu']
            instance=menu.save(commit=False)
            instance.table_number=Table.objects.get(table_number=table)
            instance.save()
            for i in item:
                instance.ordermenu.add(i)

            
            return render(request,"menu/order_succes.html")
            
    else:
        menu = OrderForm()
            
    return render(request,"menu/order.html",{"menu":menu})
    
def alltable(request):
    table=Table_Order.objects.all()
    for i in table:
        print(str(i.table_number))
        print(i.ordermenu.all())
    return render(request,"menu/alltable.html",{"table":reversed(table)})


def addmenu(request):
    if request.method=='POST':
        menu=MenuForm(request.POST,request.FILES)
        if menu.is_valid():
            menu.save()
            
    else:
        menu = MenuForm()
    return render(request, "menu/addmenu.html", {"menu": menu})


def home(request):
    
    return render(request,"menu/home.html")
