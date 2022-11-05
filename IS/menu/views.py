from django.shortcuts import render

from .forms import *


# Create your views here.

def order(request,table):
    if request.method == 'POST':
        menu=OrderForm(request.POST,request.FILES)
        if menu.is_valid():
            instance=menu.save(commit=False)
            
            instance.table_number=table
            
            instance.save()
            
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